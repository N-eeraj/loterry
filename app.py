from flask import Flask
from flask.templating import render_template

app = Flask(__name__)
app.secret_key = "xyz"

@app.route('/')
def main():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug = True)