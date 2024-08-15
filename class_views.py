from flask.views import MethodView
from flask import render_template
from flask import abort

class Careers(MethodView):

    def get(self,link_type=None):
        if link_type is None:
            return render_template("careers.html")

        link_type = link_type.rstrip('/')

        if link_type == "internship":
            return render_template("internship.html")
        
        elif link_type == "remote":
            return render_template("remote.html")
         
        elif link_type == "hybrid":
            return render_template("hybrid.html")
        
        elif link_type == "on-site":
            return render_template("on-site.html")
        
        elif link_type == "others":
            return render_template("others.html")
        
        else:
             return abort(404)
        
    
       
        

class Resources(MethodView):

    def get(self,link_type=None):
        if link_type is None:
            return render_template("resources.html")

        link_type = link_type.rstrip('/')

        if link_type == "blog":
            return render_template("blog.html")
        
        elif link_type == "documentations":
            return render_template("documetations.html")
        
        elif link_type == "new_updates":
            return render_template("new_updates.html")
        
        elif link_type == "events":
            return render_template("events.html")
        
        elif link_type == "community":
            return render_template("community.html")
        
        elif link_type == "academy":
            return render_template("academy.html")
        
        elif link_type == "partners":
            return render_template("partners.html")
        else:
             return abort(404)
        

if __name__ == "__main__":
    pass