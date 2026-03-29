# Demo Activity: Building a Rule-Based AI Flask Application

This activity shows you how to build a very simple **rule-based AI system** and connect it to a **Flask web application**.

The goal is not to build a perfect chatbot. The goal is to help you understand:
- what a rule-based AI system is
- how rules are implemented in Python
- how a front end connects to Python logic
- how the parts of a rule-based system map onto a real application

## Learning goals

By the end of this activity, you should be able to:
- explain how a rule-based AI system works
- identify the **knowledge base**, **inference engine**, and **user interface**
- run a Flask application
- edit Python rules to change the AI's behaviour
- test and improve a simple AI application

## What we are building

We are building a small web app where:
1. the user types a message into a web page
2. Flask sends that message to Python
3. a rule-based AI checks the message against a set of rules
4. the AI returns a response
5. the response is displayed back on the web page

This is useful because it turns an abstract AI idea into a working system.

## Why we are doing this

In class, you have learned that a rule-based AI system usually contains:
- a **knowledge base**
- an **inference engine**
- a **user interface**

This demo lets you see those parts in action.

### In this app
- the **knowledge base** is the set of rules in `app.py`
- the **inference engine** is the `respond()` method that checks the message and chooses a response
- the **user interface** is the `index.html` page

## Project structure

Create the following folder structure:

```text
rb_ai_flask_demo/
├── app.py
└── templates/
    └── index.html
```

Flask expects HTML files to be inside a folder called `templates`, so that folder name matters.

## Step 1: Install Flask

Open a terminal in your project folder and run:

```bash
pip install flask
```

## Step 2: Create `app.py`

This file contains:
- the Flask setup
- the rule-based AI class
- the route that handles the web page

## Step 3: Understand the logic

The `respond()` method:
- takes the user's text
- converts it to lowercase
- checks it against a sequence of rules
- returns the first matching response
- falls back to a default response if nothing matches

Example rule:

```python
elif "methodology" in message:
    return "In your methodology, explain your dataset, your rules, your tools, and how you evaluated the system."
```

This means:

> IF the message contains `"methodology"`  
> THEN return the methodology help response

## Step 4: Create `templates/index.html`

This is the front end.
It:
- displays the form
- collects user input
- shows the AI response

The form sends the message back to Flask using `POST`.

## Step 5: Run the app

In the terminal, run:

```bash
python app.py
```

Flask should show a local address, usually:

```text
http://127.0.0.1:5000/
```

Open that in your browser.

## Step 6: Test the app

Try:
- `hello`
- `what is rule-based ai`
- `how should I revise`
- `assessment`
- `methodology`
- `bye`
- `tell me about dragons`

Notice that:
- some inputs match rules
- unknown inputs get the default response

This shows both the usefulness and the limits of rule-based AI.

## Step 7: Improve the app

Add your own rules for:
- lectures
- workshops
- office hours
- referencing
- datasets
- revision strategies

Example:

```python
elif "reference" in message or "citation" in message:
    return "Use academic sources and make sure your in-text citations match your reference list."
```

## Step 8: Link back to theory

### Knowledge base
The rules in `respond()` act as the knowledge base.

### Inference engine
The `if / elif / else` structure acts as the inference process.

### User interface
The HTML page is the user interface.

## Step 9: Reflect on limitations

This app may struggle when:
- the user phrases questions differently
- the topic is too broad
- too many rules are needed
- the problem requires learning from data

That is why machine learning is often used for more complex problems.

## Success criteria

You have completed the task if:
- the Flask app runs
- the webpage accepts user input
- the AI returns responses
- you can explain the role of each part of the system
- you have added at least two of your own rules
