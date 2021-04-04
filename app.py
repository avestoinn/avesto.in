from flask import Flask, render_template

app = Flask(__name__)


# We are on technical works at the moment
@app.route('/')
def index_page():
    return render_template("index.html")
