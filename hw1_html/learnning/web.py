from flask import Flask, render_template

app = Flask(__name__)

@app.route("/show")
def index():
    return render_template("index.html")

@app.route("/next_one")
def next_one():
    return "next one"

print(__name__)

if __name__ == '__main__':
    app.run()