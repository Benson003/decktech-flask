from flask import render_template
from routes import class_views as cl
from models import models
from models import data_handler as dl

def register_routes(app):
    @app.route("/")#The landing page
    def index():
        return render_template("./main_pages/index.html")
    
    @app.route("/aboutUs/")#The about us page
    def aboutUs():
        return render_template("./main_pages/aboutUs.html")

    @app.route("/meetTheTeam/")#The meet the team page
    def meetTheTeam():
        return render_template("./main_pages/meetTheTeam.html")

    @app.route("/products/")#The products page 
    def products():
        return render_template("./main_pages/products.html")
    
    @app.route("/contactUs/")#The contact us
    def  contactUs():
        return render_template("./main_pages/contactUs.html")

    app.add_url_rule("/careers/",view_func=cl.Careers.as_view('career_base'))
    app.add_url_rule("/careers/<string:link_type>",view_func=cl.Careers.as_view('career_type'))#The dynamic link system for careers section
    app.add_url_rule("/resources/",view_func=cl.Resources.as_view('resources_base'))
    app.add_url_rule("/resources/<string:link_type>",view_func=cl.Resources.as_view('resources_links'))#The dynmic link system for the resources section
    app.add_url_rule("/admin/",view_func=cl.Admin.as_view('admin_base'))
    app.add_url_rule("/admin/<string:link_type>",view_func=cl.Admin.as_view('admin_links'))
