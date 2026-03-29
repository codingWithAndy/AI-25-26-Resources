from flask import Flask, render_template, request, Response, session, redirect, url_for
from ollama import Client
from werkzeug.datastructures import Headers
import os
from datetime import datetime
import uuid 
import json

# Initialize the Flask application
app = Flask(__name__)

# 💡 IMPORTANT: Set a secret key for session management!
# CHANGE THIS KEY TO A LONG, RANDOM STRING IN A REAL APPLICATION
app.secret_key = 'your_super_secret_key_for_log_tracking'

# Initialize the Ollama Client
client = Client()

# --- Conversation History Storage ---
conversation_history = []

# --- Ollama Chat Functionality ---
def get_ollama_response(user_input):
    """Sends user input and history to Ollama and streams the response."""
    

    # 1. Add the new user message to the history for the API call
    conversation_history.append({'role': 'user', 'content': user_input})

    full_response = ""
    # Use the entire conversation_history list as the 'messages' argument
    try:
        # Note: I'm using a model like 'gemma:2b' for compatibility. Use the model you've pulled.
        for part in client.chat('gpt-oss:120b-cloud', messages=conversation_history, stream=True):
            full_response += part['message']['content']
            
        # 2. Add the full assistant response to the history after it's complete
        conversation_history.append({'role': 'assistant', 'content': full_response})
        
        return full_response
    except Exception as e:
        # 3. If there's an error, remove the user message that was just added 
        # (to prevent a partial conversation entry)
        if conversation_history and conversation_history[-1]['role'] == 'user':
             conversation_history.pop()
        return f"Error: {e}. Is the Ollama server running?"


# --- Flask Web Route Update ---

@app.route("/", methods=["GET", "POST"])
def index():
    """Handles the main chat page and manages history."""        
    
    if request.method == "POST":
        user_input = request.form["user_input"]
        # The function handles appending the user and assistant messages
        get_ollama_response(user_input)
    
    # Render the template, passing the complete conversation history
    return render_template("index.html", history=conversation_history)

if __name__ == "__main__":
    app.run(debug=True)