# Rule-Based AI Flask Starter

This starter project gives you a basic Flask app and HTML page so that you can focus on building the **rule-based AI logic**.

## Project structure

```text
rb_ai_flask_starter/
├── app.py
├── README.md
└── templates/
    └── index.html
```

## What you are building

You will create a simple web app where:

1. a user types a message into a webpage
2. Flask sends that message to your Python code
3. your rule-based AI checks the message against rules
4. the AI returns a response to the webpage

---

## Step 1: Create a project folder

Create a folder called:

```text
rb_ai_flask_starter
```

Inside it, create:

- `app.py`
- a folder called `templates`
- inside `templates`, create `index.html`

This starter pack already includes those files.

---

## Step 2: Install Flask

Open a terminal in your project folder and run:

```bash
pip install flask
```

You may also want to check the install:

```bash
pip show flask
```

---

## Step 3: Understand the role of each file

### `app.py`
This is the main Python file. It:
- starts the Flask app
- accepts messages from the form
- sends the message to your rule-based AI
- returns the answer to the webpage

### `templates/index.html`
This is the webpage. It:
- displays the text box
- lets the user type a message
- shows the AI response

---

## Step 4: Read the starter code in `app.py`

There are three main parts:

### 1. Flask setup
```python
from flask import Flask, render_template, request

app = Flask(__name__)
```

### 2. The AI class
```python
class RuleBasedAI:
    def respond(self, message: str) -> str:
        ...
```

This is where you write the **AI logic**.

### 3. The route
```python
@app.route("/", methods=["GET", "POST"])
def index():
    ...
```

This tells Flask what to do when someone opens the webpage or submits the form.

---

## Step 5: Build the AI logic

Start with a very small set of rules.

Example:

```python
if "hello" in message:
    return "Hello! How can I help you today?"
elif "deadline" in message:
    return "Check Minerva for the latest deadlines."
elif "bye" in message:
    return "Goodbye!"
else:
    return "I'm sorry, I don't understand that yet."
```

### Your minimum goal
Add at least:

- 1 greeting rule
- 1 information rule
- 1 help/advice rule
- 1 farewell rule
- 1 default response

---

## Step 6: Test your rules before running Flask

Before launching the app, test your logic mentally or by writing test inputs.

Example test plan:

- `"hello"` → greeting response
- `"when is the deadline"` → deadline response
- `"can you help me revise"` → revision/help response
- `"bye"` → farewell response
- `"what is quantum cheese"` → default response

---

## Step 7: Run the app

In the terminal, run:

```bash
python app.py
```

Flask should display a local address, often:

```text
http://127.0.0.1:5000/
```

Open that in your browser.

---

## Step 8: Improve the app

Once the basic version works, try one or more of these:

### Option A: Add more rules
Add support for:
- assessment
- lectures
- revision
- office hours

### Option B: Add multiple-condition rules
Example:

```python
elif "deadline" in message and "coursework" in message:
    return "Please check the coursework area on Minerva."
```

### Option C: Add synonyms
Example:

```python
elif "exam" in message or "test" in message:
    return "Try using active recall and short revision sessions."
```

### Option D: Change the domain
Instead of a university assistant, build:
- a laptop troubleshooting assistant
- a simple symptom checker
- a movie recommendation helper
- a weather advice bot

---

## Step 9: Reflect on the AI components

When your app is finished, identify:

- **Knowledge base** → where are the rules stored?
- **Inference engine** → where are decisions made?
- **User interface** → what does the user interact with?

---

## Scaffolded checklist

Use this checklist as you work:

- [ ] Flask installed
- [ ] Project folder created
- [ ] `app.py` created
- [ ] `templates/index.html` created
- [ ] App runs in browser
- [ ] At least 4 rules added
- [ ] Default response added
- [ ] Rules tested
- [ ] App improved with one extension

---

## Common mistakes

### The page does not load
Check:
- Flask is installed
- you ran `python app.py`
- `index.html` is inside the `templates` folder

### The form works but always returns the default response
Check:
- your keywords match the user input
- you converted the message to lowercase
- your `if / elif / else` logic is in the right order

### I get an indentation error
Python is sensitive to indentation. Make sure blocks line up correctly.

### My rule never runs
A broader rule may be matching first. Put more specific rules above more general ones.

---

## Suggested extension task

Turn this into a more realistic **rule-based AI system** by:
- choosing a domain
- writing 6–10 rules
- testing with at least 8 user inputs
- explaining the system using the terms:
  - knowledge base
  - inference engine
  - user interface
