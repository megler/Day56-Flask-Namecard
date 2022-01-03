# nameCard.py
#
# Python Bootcamp Day 56 - Flask Name Card
# Usage:
#      A simple name card made with Flask and HTML templates. Day 56 Python Bootcamp
#
# Marceia Egler January 3, 2022

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
