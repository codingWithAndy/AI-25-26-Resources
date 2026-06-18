from flask import Flask, render_template, request

app = Flask(__name__)


class RuleBasedAI:
    def respond(self, message: str) -> str:
        """Return a response based on simple rules."""
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
