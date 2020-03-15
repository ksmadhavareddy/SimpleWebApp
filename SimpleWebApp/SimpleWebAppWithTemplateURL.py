from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return  render_template('name.html')

@app.route("/info")
def indexinfo():
    myvariable = "madhava"
    return  render_template('name.html',myvar=myvariable)
 

if __name__ == "__main__":
    app.run(debug=True)