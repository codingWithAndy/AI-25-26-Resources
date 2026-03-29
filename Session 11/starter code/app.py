from flask import Flask, render_template, request, Response, session, redirect, url_for
from ollama import Client
from werkzeug.datastructures import Headers
import os
from datetime import datetime
import uuid 
import json

# Initialize the Flask application
app = Flask(__name__)


# --- Flask Web Route Update ---

@app.route("/", methods=["GET", "POST"])
def index():
    """Handles the main chat page and manages history."""        

    # Render the template, passing the complete conversation history
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)