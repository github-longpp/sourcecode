from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == 'GET':
        return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)