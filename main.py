from flask import Flask, render_template
import sqlalchemy

app = Flask(__name__)

@app.route("/")
def user():
    return render_template("index.html")

@app.route("/skaiciavimai")
def skaiciavimai():
    return render_template("skaiciavimai.html")

@app.route("/zmones")
def zmones():
    vardai = ['Jonas', 'Antanas', 'Petras']
    return render_template("zmones.html", sarasas=vardai)

if __name__ == "__main__":
    app.run(debug=True)