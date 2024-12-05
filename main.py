from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def user():
    return render_template("index.html")

@app.route("/skaiciavimai")
def skaiciavimai():
    return render_template("skaiciavimai.html")

if __name__ == "__main__":
    app.run(debug=True)