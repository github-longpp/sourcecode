from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Welcome to VietNam, ahha"

@app.route("/long")
def hello_long():
    return "Hello Long"

@app.route("/<name>")
def praise(name):
    return name

# @app.route("/add/<x>/<y>")
# def add(x,y):
#     s = int(x) + int(y)
#     s = str(s)
#     return s

@app.route("/add/<int:x>/<int:y>")
def add(x,y):
    s = x + y
    return str(s)

@app.route("/question")
def show_question():
    return render_template("question.html")

if __name__ == "__main__":
    app.run(debug=True)