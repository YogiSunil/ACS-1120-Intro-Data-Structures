"""Main script, uses other modules to generate sentences."""
from flask import Flask
import random

app = Flask(__name__)


# Example word list (replace this with a more advanced model)
word_list = ["hello", "world", "flask", "python", "sentence", "generate", "random"]

@app.route("/")
def home():
    """Return a randomly selected word from the list."""
    random_word = random.choice(word_list)
    return f"<p>{random_word}</p>"

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
