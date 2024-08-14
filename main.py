from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/products")
def projects():
    return render_template("products.html")

@app.route("/contact_us")
def contactUs():
    return render_template("contact_us.html")

@app.route("/meet_the_team")
def meetTheTeam():
    return render_template("meet_the_team.html")




if __name__ == "__main__":
    app.run()
