from flask import Flask, render_template, request
import random

app = Flask(__name__)

# List of placeholders for personalization
placeholders = ["[Name]", "[Date]", "[Message]"]

# List of sample messages
sample_messages = [
    "Dear [Name],\nI wanted to let you know how much I love you...",
    "My dearest [Name],\nEvery moment with you feels like a blessing...",
    "[Name],\nFrom the moment we met, my life has been filled with joy..."
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        date = request.form.get("date")
        message = random.choice(sample_messages).replace("[Name]", name).replace("[Date]", date)
        return render_template("index.html", generated_message=message)
    return render_template("index.html", generated_message="")

if __name__ == "__main__":
    app.run(debug=True)
