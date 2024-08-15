from flask import Flask
from flask import render_template
import class_views as cl

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aboutUs")
def aboutUs():
    return render_template("aboutUs.html")

@app.route("/meetTheTeam")
def meetTheTeam():
    return render_template("meetTheTeam.html")

@app.route("/products")
def products():
    return render_template("products.html")
 
@app.route("/contactUs")
def  contactUs():
    return render_template("contactUs.html")

app.add_url_rule('/careers/<string:link_type>',view_func=cl.Careers.as_view('career_type'))
app.add_url_rule('/resources/<string:link_type>',view_func=cl.Resources.as_view('resources'))

if __name__ == "__main__":
    app.run()