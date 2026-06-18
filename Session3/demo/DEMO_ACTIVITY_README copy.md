# Demo Activity: Building a Rule-Based AI Flask Application

This guide shows you **step by step** how to build a simple **rule-based AI system** inside a **Flask web application**.

The aim is to help you understand both:

- **how rule-based AI works**
- **how a Python back end connects to a web front end**

This is not about building a perfect chatbot.  
It is about learning how the main parts of a rule-based system fit together in a working application.

---

# 1. What are we building?

We are building a small web app where:

1. a user types a message into a web page
2. that message is sent to Python using Flask
3. Python checks the message against a set of rules
4. the program chooses a response
5. the response is displayed back on the page

For example:

- user types: `hello`
- system checks the rules
- system returns: `Hello! I am your rule-based AI study assistant.`

---

# 2. Why are we doing this?

In class, you learned that a rule-based AI system usually has three main parts:

## Knowledge base
This stores the rules.

Example:
- IF the message contains `"hello"` THEN return a greeting

## Inference engine
This checks which rule matches and decides what to do.

## User interface
This is what the user interacts with.

In this app:

- the **knowledge base** is the set of rules in `app.py`
- the **inference engine** is the `respond()` method
- the **user interface** is the `index.html` page

So this activity helps you connect **theory** to **implementation**.

---

# 3. What you need before you start

You should have:

- Python installed
- VS Code or another code editor
- basic understanding of:
  - variables
  - if statements
  - functions
  - classes
- internet access to install Flask

---

# 4. Stage 1: Create the project folder

Create a folder called:

```text
rb_ai_flask_demo
```

Inside that folder, create:

```text
rb_ai_flask_demo/
├── app.py
└── templates/
    └── index.html
```

## Why?
Flask expects HTML pages to be stored inside a folder called `templates`.

If your `index.html` file is not inside `templates`, Flask will not find it.

---

# 5. Stage 2: Install Flask

Open a terminal inside your project folder and run:

```bash
pip install flask
```

## Why?
Flask is the framework that lets us:

- create a web server
- define routes
- receive form input
- display HTML pages

You can check Flask installed correctly with:

```bash
pip show flask
```

---

# 6. Stage 3: Create the basic Flask app

Open `app.py` and add this code:

```python
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello from Flask!"


if __name__ == "__main__":
    app.run(debug=True)
```

## What this does

### Import line
```python
from flask import Flask, render_template, request
```

This imports the tools we need:
- `Flask` → creates the app
- `render_template` → loads HTML files
- `request` → gets data sent from a form

At this point, you are not using all of them yet, but you will later.

### Create the app
```python
app = Flask(__name__)
```

This creates the Flask application.

### Create a route
```python
@app.route("/")
def index():
    return "Hello from Flask!"
```

This says:

> when the user visits the home page `/`, run the `index()` function

### Run the app
```python
if __name__ == "__main__":
    app.run(debug=True)
```

This starts the development server.

---

# 7. Stage 4: Test the basic app

Run:

```bash
python app.py
```

You should see a message showing a local address, usually:

```text
http://127.0.0.1:5000/
```

Open that address in your browser.

You should see:

```text
Hello from Flask!
```

## Why do this first?
This confirms:
- Flask is installed correctly
- your file runs
- your route works

It is good practice to test a simple version before adding more features.

---

# 8. Stage 5: Replace the text response with an HTML page

Now create the file:

```text
templates/index.html
```

Add this code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rule-Based AI Demo</title>
</head>
<body>
    <h1>Rule-Based AI Demo</h1>
    <p>This is the front end of the application.</p>
</body>
</html>
```

Now update `app.py` to this:

```python
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
```

## Why?
Instead of returning plain text, Flask now loads an HTML page.

This gives us a proper **user interface**.

---

# 9. Stage 6: Add a form to collect user input

Now replace the contents of `templates/index.html` with this:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rule-Based AI Demo</title>
</head>
<body>
    <h1>Rule-Based AI Demo</h1>

    <form method="POST">
        <label for="message">Your message:</label>
        <input type="text" id="message" name="message">
        <button type="submit">Send</button>
    </form>
</body>
</html>
```

## What this does

### Form
```html
<form method="POST">
```

This creates a form that sends the user's input to the server.

### Text box
```html
<input type="text" id="message" name="message">
```

This is where the user types a message.

The `name="message"` part matters because Flask will use that name to retrieve the input.

### Button
```html
<button type="submit">Send</button>
```

This submits the form.

---

# 10. Stage 7: Update Flask so it can receive the message

Now update `app.py` like this:

```python
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    user_message = ""

    if request.method == "POST":
        user_message = request.form.get("message", "")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
```

## What changed?

### Allow GET and POST
```python
@app.route("/", methods=["GET", "POST"])
```

- `GET` = load the page
- `POST` = submit the form

### Get the user input
```python
user_message = request.form.get("message", "")
```

This reads whatever the user typed into the input field called `message`.

## Why?
Before this, the form existed but Flask did not do anything with the submitted data.

Now the back end can receive the message.

---

# 11. Stage 8: Create the rule-based AI class

Now add a class to `app.py`:

```python
class RuleBasedAI:
    def respond(self, message: str) -> str:
        message = message.lower().strip()

        if "hello" in message or "hi" in message:
            return "Hello! I am your rule-based AI study assistant."
        elif "deadline" in message or "assessment" in message:
            return "Please check your module page for the latest assessment deadlines and guidance."
        elif "revise" in message or "revision" in message or "study" in message:
            return "Try breaking the topic into smaller parts and testing yourself with short practice questions."
        elif "rule-based ai" in message or "symbolic ai" in message:
            return "Rule-based AI uses explicit if-then rules written by humans to make decisions."
        elif "methodology" in message:
            return "In your methodology, explain your dataset, your rules, your tools, and how you evaluated the system."
        elif "bye" in message or "goodbye" in message:
            return "Goodbye! Keep testing your rules carefully."
        else:
            return "I am not sure how to answer that yet. Try asking about deadlines, revision, methodology, or rule-based AI."
```

Then create an object from the class:

```python
ai = RuleBasedAI()
```

## Why?
This is the core AI logic.

The method:
```python
respond(self, message: str) -> str
```

takes a message and returns a response based on rules.

---

# 12. Stage 9: Understand the AI logic

Look at this line:

```python
message = message.lower().strip()
```

## Why do this?
It makes the input easier to match.

For example:
- `Hello`
- `hello`
- ` HELLO `

all become:

```python
hello
```

This makes the rules more reliable.

Now look at a rule:

```python
elif "methodology" in message:
    return "In your methodology, explain your dataset, your rules, your tools, and how you evaluated the system."
```

This means:

> IF the word `"methodology"` appears in the message  
> THEN return the methodology response

That is the rule-based idea:
- check a condition
- return an action or conclusion

---

# 13. Stage 10: Connect the form to the AI

Now update the `index()` function in `app.py` so that it sends the user's message to the AI.

Use this full version:

```python
from flask import Flask, render_template, request

app = Flask(__name__)


class RuleBasedAI:
    def respond(self, message: str) -> str:
        message = message.lower().strip()

        if "hello" in message or "hi" in message:
            return "Hello! I am your rule-based AI study assistant."
        elif "deadline" in message or "assessment" in message:
            return "Please check your module page for the latest assessment deadlines and guidance."
        elif "revise" in message or "revision" in message or "study" in message:
            return "Try breaking the topic into smaller parts and testing yourself with short practice questions."
        elif "rule-based ai" in message or "symbolic ai" in message:
            return "Rule-based AI uses explicit if-then rules written by humans to make decisions."
        elif "methodology" in message:
            return "In your methodology, explain your dataset, your rules, your tools, and how you evaluated the system."
        elif "bye" in message or "goodbye" in message:
            return "Goodbye! Keep testing your rules carefully."
        else:
            return "I am not sure how to answer that yet. Try asking about deadlines, revision, methodology, or rule-based AI."


ai = RuleBasedAI()


@app.route("/", methods=["GET", "POST"])
def index():
    user_message = ""
    response = ""

    if request.method == "POST":
        user_message = request.form.get("message", "")
        response = ai.respond(user_message)

    return render_template(
        "index.html",
        user_message=user_message,
        response=response
    )


if __name__ == "__main__":
    app.run(debug=True)
```

## What is new here?

### Create a response variable
```python
response = ""
```

This stores the AI's reply.

### Call the AI
```python
response = ai.respond(user_message)
```

This sends the user's message into the rule-based system.

### Pass data to the HTML page
```python
return render_template(
    "index.html",
    user_message=user_message,
    response=response
)
```

This sends the variables to the HTML page so they can be displayed.

---

# 14. Stage 11: Update the HTML to show the AI response

Now replace `templates/index.html` with this:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rule-Based AI Demo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            background: #f8f9fb;
            color: #222;
            line-height: 1.6;
        }

        .container {
            background: white;
            border: 1px solid #ddd;
            border-radius: 12px;
            padding: 24px;
        }

        input[type="text"] {
            width: 100%;
            padding: 12px;
            margin: 12px 0;
            box-sizing: border-box;
        }

        button {
            padding: 10px 16px;
            cursor: pointer;
        }

        .message-box {
            margin-top: 20px;
            padding: 16px;
            background: #f1f3f5;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Rule-Based AI Demo</h1>

        <form method="POST">
            <label for="message"><strong>Your message</strong></label>
            <input
                type="text"
                id="message"
                name="message"
                placeholder="Type a message for the AI"
                value="{{ user_message }}"
            >
            <button type="submit">Send</button>
        </form>

        {% if response %}
        <div class="message-box">
            <strong>AI response:</strong>
            <p>{{ response }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
```

## What is important here?

### Display previous input
```html
value="{{ user_message }}"
```

This keeps the user's message in the box after submitting.

### Conditionally display the response
```html
{% if response %}
```

This means:
- if there is a response, show it
- if there is no response yet, do not show the response area

This is part of Flask's templating system.

---

# 15. Stage 12: Run and test the full app

Run:

```bash
python app.py
```

Open the local address in your browser.

Try these messages:

- `hello`
- `what is rule-based ai`
- `how should I revise`
- `assessment`
- `methodology`
- `bye`
- `tell me about dragons`

## What should happen?
Some messages should match a rule and get a specific reply.

Unknown messages should get the default response.

---

# 16. Stage 13: Test your system properly

Create a small test table like this:

| Input | Expected output |
|---|---|
| hello | greeting |
| methodology | methodology guidance |
| bye | farewell |
| revise for exam | revision advice |
| random question | default response |

## Why?
Testing is important because rule-based systems only behave as well as their rules.

---

# 17. Stage 14: Extend the app

Once your app works, improve it by adding more rules.

## Example additions

### Referencing support
```python
elif "reference" in message or "citation" in message:
    return "Use academic sources and make sure your in-text citations match your reference list."
```

### Lecture support
```python
elif "lecture" in message:
    return "Review your session slides and notes before attempting the task."
```

### Office hours
```python
elif "office hours" in message:
    return "Please check the module site or ask your lecturer for current office hour details."
```

---

# 18. Stage 15: Reflect on the theory

Now link the app back to the lecture.

## Where is the knowledge base?
The rules inside `respond()`.

## Where is the inference engine?
The `if / elif / else` logic that checks the message and selects a response.

## Where is the user interface?
The `index.html` page.

---

# 19. Stage 16: Think about limitations

This app is useful for learning, but it has limitations.

It may struggle when:

- a user phrases a question in an unexpected way
- too many rules are needed
- the domain becomes too complex
- ambiguity is present
- learning from data would be more useful

That is one reason machine learning became important in AI.

---

# 20. Full final code

## `app.py`

```python
from flask import Flask, render_template, request

app = Flask(__name__)


class RuleBasedAI:
    def respond(self, message: str) -> str:
        message = message.lower().strip()

        if "hello" in message or "hi" in message:
            return "Hello! I am your rule-based AI study assistant."
        elif "deadline" in message or "assessment" in message:
            return "Please check your module page for the latest assessment deadlines and guidance."
        elif "revise" in message or "revision" in message or "study" in message:
            return "Try breaking the topic into smaller parts and testing yourself with short practice questions."
        elif "rule-based ai" in message or "symbolic ai" in message:
            return "Rule-based AI uses explicit if-then rules written by humans to make decisions."
        elif "methodology" in message:
            return "In your methodology, explain your dataset, your rules, your tools, and how you evaluated the system."
        elif "bye" in message or "goodbye" in message:
            return "Goodbye! Keep testing your rules carefully."
        else:
            return "I am not sure how to answer that yet. Try asking about deadlines, revision, methodology, or rule-based AI."


ai = RuleBasedAI()


@app.route("/", methods=["GET", "POST"])
def index():
    user_message = ""
    response = ""

    if request.method == "POST":
        user_message = request.form.get("message", "")
        response = ai.respond(user_message)

    return render_template(
        "index.html",
        user_message=user_message,
        response=response
    )


if __name__ == "__main__":
    app.run(debug=True)
```

## `templates/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rule-Based AI Demo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            background: #f8f9fb;
            color: #222;
            line-height: 1.6;
        }

        .container {
            background: white;
            border: 1px solid #ddd;
            border-radius: 12px;
            padding: 24px;
        }

        input[type="text"] {
            width: 100%;
            padding: 12px;
            margin: 12px 0;
            box-sizing: border-box;
        }

        button {
            padding: 10px 16px;
            cursor: pointer;
        }

        .message-box {
            margin-top: 20px;
            padding: 16px;
            background: #f1f3f5;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Rule-Based AI Demo</h1>

        <form method="POST">
            <label for="message"><strong>Your message</strong></label>
            <input
                type="text"
                id="message"
                name="message"
                placeholder="Type a message for the AI"
                value="{{ user_message }}"
            >
            <button type="submit">Send</button>
        </form>

        {% if response %}
        <div class="message-box">
            <strong>AI response:</strong>
            <p>{{ response }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
```

---

# 21. Final success criteria

You have completed the activity if:

- your Flask app runs
- the page loads in the browser
- the user can submit a message
- the AI returns a response
- you can explain knowledge base, inference engine, and user interface
- you have added at least two of your own rules
