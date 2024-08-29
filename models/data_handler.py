from models import models
from app import db
import bcrypt
class User():
    def __init__(self):
        pass

    def get_all_users(self):
        models.User.query.all()


    def get_specfic_user(self,id):
        models.User.query.filter(models.User.id == id).first()

    
    def create_user(self,username,first_name,last_name,bio,password): 
        gen_salt = bcrypt.gensalt()

        encoded_password = password.encode('utf_8')

        hashed_password = bcrypt.hashpw(encoded_password,gen_salt)


        person = models.User(
                            username=username,
                             first_name=first_name,
                             last_name=last_name,
                             bio=bio,
                             password=hashed_password
                             )
        
        db.session.add(person)
        db.session.commit()


class Blog():
    def __init__(self):
        pass

    def read_all_blogs(self):
        blogs = models.Blog.query.all()
        return blogs

    def read_specfic_blog(self,id):
        blog = models.Blog.query.filter(models.Blog.id == id).first()
        return blog
    
    def create_blog(self,title,content,user_id):
        blog = models.Blog(title=title,content=content,user_id=user_id)
        try:
            db.session.add(blog)
            db.session.commit()
        except:
            db.session.rollback()

    def delete_specfic_blog(self,id):
        blog = models.Blog.query.filter(models.Blog.id == id).first() 
        try:
            db.session.delete(blog)       
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f"Failed delete procdure.\n Possible Reason:{e}"



class Projects():
    def __init__(self):
        pass

    def read_all_projects(self):
        models.Projects.query.all()

    def read_spefic_project(self,id):
        project = models.Projects.query.filter(models.Projects.id == id).first()
        return project

    def create_project(self,title,content):
        project = models.Projects(title=title,content=content)
        
        try:
            db.session.add(project)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            return f"Failed add procdure. \n Possible Resason:{e}"
            
    def delete_specfic_project(self,id):
        blog = models.Blog.query.filter(models.Blog.id == id).first()
         
        try:
            db.session.delete(blog)       
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f"Failed delete procdure.\n Possible Reason:{e}"
