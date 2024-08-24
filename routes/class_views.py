from flask.views import MethodView
from flask import render_template
from flask import abort
from models import models


class Careers(MethodView):

    def get(self,link_type=None):
        if link_type is None:
            return render_template("./main_pages/careers_pages/careers.html")

        link_type = link_type.rstrip("/")

        if link_type == "internship":
            return render_template("./main_pages/career_pages/internship.html")
        
        elif link_type == "remote":
            return render_template("./main_pages/career_pages/remote.html")
         
        elif link_type == "hybrid":
            return render_template("./main_pages/career_pages/hybrid.html")
        
        elif link_type == "on-site":
            return render_template("./main_pages/career_pages/on-site.html")
        
        elif link_type == "others":
            return render_template("./main_pages/career_pages/others.html")
        
        else:
             return abort(404)

class Resources(MethodView):

    def get(self,link_type=None):
        if link_type is None:
            return render_template("./main_pages/resources_pages/resources.html")

        link_type = link_type.rstrip("/")

        if link_type == "blog":
            
            return render_template("./main_pages/resources_pages/blog.html")
        
        elif link_type == "documentations":
            return render_template("./main_pages/resources_pages/documetations.html")
        
        elif link_type == "new_updates":
            return render_template("./main_pages/resources_pages/new_updates.html")
        
        elif link_type == "events":
            return render_template("./main_page/resources_pages/events.html")
        
        elif link_type == "community":
            return render_template("./main_pages/career_pages/community.html")
        
        elif link_type == "academy":
            return render_template("./main_pages/career_pages/academy.html")
        
        elif link_type == "partners":
            return render_template("./main_pages/career_pages/partners.html")
        else:
             return abort(404)
        

if __name__ == "__main__":
    pass