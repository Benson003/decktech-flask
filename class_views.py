from flask.views import MethodView
from flask import render_template

class Careers(MethodView):

    def get(self,link_type):
        if "internship" == link_type:
            return render_template("internship.html")
        
        elif "remote" == link_type:
            return render_template("remote.html")
         
        elif "hybrid" == link_type:
            return render_template("hybrid.html")
        
        elif "on-site" == link_type:
            return render_template("on-site.html")
        
        elif "others" == link_type:
            return render_template("others.html")
        
        elif "" == link_type:
            return render_template("carreers.html")
        
        else:
            return 404
        

class Resources(MethodView):

    def get(self,link_type):
        if "blog" == link_type:
            return render_template("blog.html")
        
        elif "documentations" == link_type:
            return render_template("documetations.html")
        
        elif "news_updates" == link_type:
            return render_template("new_updates.html")
        
        elif "events" == link_type:
            return render_template("community.html")
        
        elif "academy" == link_type:
            return render_template("academy.html")
        
        elif "partners" == link_type:
            return render_template("partners.html")
        elif "" == link_type:
            return render_template("resources.html")
        else:
            return 404
        

if __name__ == "__main__":
    pass