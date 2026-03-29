# Step-by-Step Guide: Building a Flask + Ollama Chatbot

## Lesson Goal
Build a working chatbot web application using **Flask**, **Ollama**, and a simple **HTML/Markdown front-end**.

This guide is written in a building-block manner for students to follow.

---

## Project Setup
Create a new folder:

```
flask-ollama-chatbot/
```

Inside it create:
```
app.py
templates/
    index.html
```

---

## 1. Install Dependencies
In the project folder run:

```bash
pip install flask ollama werkzeug
```

Ensure Ollama is running:

```bash
ollama serve
```

Optional: pull a model:

```bash
ollama pull gpt-oss:120b-cloud
# or
ollama pull llama3
```

---

## 2. STEP-BY-STEP: Build `app.py` (building blocks)

### STEP 2.1 — Imports
Add the required imports:

```python
from flask import Flask, render_template, request, session
from ollama import Client
import uuid
```

### STEP 2.2 — Initialise Flask
Create the Flask app and set a secret key:

```python
app = Flask(__name__)
app.secret_key = 'your_super_secret_key_for_log_tracking'  # replace in real apps
```

### STEP 2.3 — Initialise Ollama Client
Create a client to talk to the local Ollama server:

```python
client = Client()
```

### STEP 2.4 — Conversation Store
Start with a simple conversation storage (a list for single-user):

```python
conversation_history = []
```

> Note: for multi-user sessions you can use `session` with a dict keyed by `user_id`. This guide uses a single shared history to keep things simple.

### STEP 2.5 — Function to Get Model Response
Add a function that:
- appends the user message
- streams the model output
- appends the assistant response

```python
def get_ollama_response(user_input):
    """Sends user input and history to Ollama and streams the response."""

    # 1. Add the new user message to the history for the API call
    conversation_history.append({'role': 'user', 'content': user_input})

    full_response = ""

    try:
        # Use the entire conversation_history as the messages argument
        for part in client.chat('gpt-oss:120b-cloud', messages=conversation_history, stream=True):
            full_response += part['message']['content']

        # 2. Add the assistant response to history
        conversation_history.append({'role': 'assistant', 'content': full_response})
        return full_response

    except Exception as e:
        # 3. On error, remove the last user message (prevents partial entries)
        if conversation_history and conversation_history[-1]['role'] == 'user':
            conversation_history.pop()
        return f"Error: {e}. Is the Ollama server running?"
```

### STEP 2.6 — Create the Flask Route
Create the main route that shows the chat and handles form POSTs:

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        get_ollama_response(user_input)

    return render_template('index.html', history=conversation_history)
```

### STEP 2.7 — Run the App
Add the usual runner:

```python
if __name__ == '__main__':
    app.run(debug=True)
```

---

## 3. Full `app.py` (copy/paste)

```python
from flask import Flask, render_template, request, session
from ollama import Client
import uuid

app = Flask(__name__)
app.secret_key = 'your_super_secret_key_for_log_tracking'

client = Client()
conversation_history = []

def get_ollama_response(user_input):
    """Sends user input and history to Ollama and streams the response."""
    conversation_history.append({'role': 'user', 'content': user_input})
    full_response = ""
    try:
        for part in client.chat('gpt-oss:120b-cloud', messages=conversation_history, stream=True):
            full_response += part['message']['content']
        conversation_history.append({'role': 'assistant', 'content': full_response})
        return full_response
    except Exception as e:
        if conversation_history and conversation_history[-1]['role'] == 'user':
            conversation_history.pop()
        return f"Error: {e}. Is the Ollama server running?"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        get_ollama_response(user_input)
    return render_template('index.html', history=conversation_history)

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 4. Build the Frontend (`templates/index.html`)

Create `templates/index.html` and paste the following. It renders the conversation, converts assistant Markdown to HTML using `marked.js`, and auto-scrolls to the bottom.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Ollama Scrolling Chatbot</title>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <style>
    body { font-family: Arial, sans-serif; max-width: 1020px; margin: 40px auto; padding: 20px; border: 1px solid #ccc; display:flex; flex-direction:column; height:90vh;}
    h1{text-align:center;}
    .chat-container{flex-grow:1; overflow-y:auto; border:1px solid #eee; padding:15px; margin-bottom:10px; background:#f9f9f9; display:flex; flex-direction:column;}
    .message{padding:8px 10px; margin:5px 0; border-radius:5px; max-width:80%;}
    .user-message{background:#d1e7ff; align-self:flex-end;}
    .assistant-message{background:#e9ecef; align-self:flex-start;}
    .assistant-message pre{background:#333;color:#fff;padding:10px;border-radius:5px;overflow-x:auto;}
    form{display:flex;}
    input[type='text']{flex-grow:1;padding:10px;border:1px solid #ccc;}
    button{padding:10px 15px;background:#007BFF;color:#fff;border:none;cursor:pointer;}
  </style>
</head>
<body>
  <h1>Experiment Interface</h1>
  <div class="chat-container" id="chat-container">
    {% for message in history %}
      {% if message.role == 'user' %}
        <div class="message user-message">
          <strong>You:</strong> {{ message.content }}
        </div>
      {% elif message.role == 'assistant' %}
        <div class="message assistant-message">
          <div id="msg-{{ loop.index }}" class="markdown-content"></div>
          <script id="markdown-{{ loop.index }}" type="text/markdown">
{{ message.content }}
          </script>
        </div>
      {% endif %}
    {% endfor %}
  </div>

  <form method="POST" action="/">
    <input type="text" name="user_input" placeholder="Type your message here..." required>
    <button type="submit">Send</button>
  </form>

  <script>
    const markdownScripts = document.querySelectorAll('script[type="text/markdown"]');
    markdownScripts.forEach(script => {
      const index = script.id.split('-')[1];
      const target = document.getElementById('msg-' + index);
      if (target) {
        target.innerHTML = marked.parse(script.textContent.trim());
      }
    });
    const container = document.getElementById('chat-container');
    container.scrollTop = container.scrollHeight;
  </script>
</body>
</html>
```

---

## 5. Run and Test
1. Start Ollama: `ollama serve`  
2. Start Flask: `python app.py`  
3. Open browser: `http://127.0.0.1:5000/`  
4. Send messages and observe model responses.

---

## 6. Classroom Extensions (optional, progressive)
1. **Per-user history:** use `session` + a dict keyed by `user_id`.  
2. **Streaming to browser (advanced):** use Server-Sent Events (SSE) to push partial tokens to the client.  
3. **Persistence:** store chats in a JSON file or a simple database (SQLite).  
4. **Model swapper:** add a dropdown to pick available models.  
5. **Rate limiting / safety:** filter or prompt-engineer inputs.

---

## 7. Troubleshooting Tips
- If you see `Error: ... Is the Ollama server running?` — ensure `ollama serve` is active.  
- If `client.chat` raises model-not-found — pull the model with `ollama pull <model>`.  
- If Flask shows a template error — check `templates/index.html` path and indentation.

---
