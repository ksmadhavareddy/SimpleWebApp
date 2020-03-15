from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome!"

@app.route("/info")
def info():
    return "Welcome to Information Portal Page!"

@app.route('/mypage/<name>')
def mypage(name):
    return "Welcome to Information Portal Page {}. ! ".format(name)


if __name__ == "__main__":
    app.run(debug=True)