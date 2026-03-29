from flask import Flask, render_template, request

app = Flask(__name__)


class RuleBasedAI:
    def __init__(self):
        # STEP 4:
        # Add or edit rules here if you want to use a dictionary-based approach.
        # You can also ignore this and write your logic directly in respond().
        self.rules = {
            "hello": "Hello! How can I help you today?",
            "hi": "Hi! What would you like help with?",
            # Add more rules here
        }

    def respond(self, message: str) -> str:
        """
        STEP 5:
        Complete the AI logic.

        Suggested approach:
        1. Convert the message to lowercase
        2. Check for keywords using if / elif / else
        3. Return a suitable response
        4. Include a default response if no rule matches
        """
        message = message.lower().strip()

        # Example starter rule
        if "hello" in message or "hi" in message:
            return "Hello! How can I help you today?"

        # TODO:
        # Add more rules below.
        #
        # Example ideas:
        # elif "deadline" in message:
        #     return "Check Minerva for the latest deadlines."
        #
        # elif "assessment" in message:
        #     return "Your assessment brief explains the task requirements."
        #
        # elif "bye" in message:
        #     return "Goodbye!"
        #
        # else:
        #     return "I'm sorry, I don't understand that yet."

        return "I'm sorry, I don't understand that yet."


ai = RuleBasedAI()


@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    user_message = ""

    if request.method == "POST":
        user_message = request.form.get("message", "")
        response = ai.respond(user_message)

    return render_template(
        "index.html",
        response=response,
        user_message=user_message,
    )


if __name__ == "__main__":
    # STEP 7:
    # Run this file, then open the local address shown in the terminal.
    app.run(debug=True)
