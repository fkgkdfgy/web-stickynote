from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/start")
def sign_in_or_up():
    return render_template("web.html")

if __name__ == '__main__':
    app.run(host='192.168.107.140',port=8080)
    