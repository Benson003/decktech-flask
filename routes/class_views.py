from flask.views import MethodView
from flask import render_template
from flask import abort
from models import models


career_templates =  {
            None:"./main_pages/careers_pages/careers.html",
            "internship":"./main_pages/careers_pages/internship.html",
            "remote":"./main_pages/careers_pages/remote.html",
            "hybrid":"./main_pages/careers_pages/hybrid.html",
            "on-site":"./main_pages/careers_pages/on-site.html",
            "others":"./main_pages/careers_pages/others.html",
        }

resources_templates = {
            None:"./main_pages/resources_pages/resources.html",
            "blog":"./main_pages/resources_pages/blog.html",
            "documentations":"./main_pages/resources_pages/documetations.html",
            "new_updates":"./main_pages/resources_pages/new_updates.html",
            "events":"./main_page/resources_pages/events.html",
            "community":"./main_pages/resources_pages/community.html",
            "academy":"./main_pages/resources_pages/academy.html",
            "partners":"./main_pages/resources_pages/partners.html"
        }



class Careers(MethodView):

    def get(self,link_type=None):
        templates =career_templates
        link_type = link_type.strip().lower().rstrip("/") if link_type else None
        template = templates.get(link_type)

        return render_template(template) if template else abort(404)
        
    
class Resources(MethodView):

    def get(self,link_type=None):
       
        templates = resources_templates
        link_type = link_type.strip().lower().rstrip("/")if link_type else None
        template = templates.get(link_type)
        return render_template(template)if template else abort(404)

if __name__ == "__main__":
    pass