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






class Applicants():


    def add_applicant(self,fullname, role):
        try:
            role_enum = models.JobType[role.upper().replace(" ", "_")]
        except KeyError:
            raise ValueError("Invalid job type provided")

        applicant = Applicants(fullname=fullname, role=role_enum)
        db.session.add(applicant)
        db.session.commit()
        return applicant


    def get_applicant_by_id(self,applicant_id):
        return Applicants.query.get(applicant_id)


    def get_all_applicants(self):
        return Applicants.query.all()


    def update_applicant(self,applicant_id, fullname=None, role=None):
        applicant = Applicants.query.get(applicant_id)
        if not applicant:
            raise ValueError("Applicant not found")

        if fullname:
            applicant.fullname = fullname
        if role:
            try:
                applicant.role = models.JobType[role.upper().replace(" ", "_")]
            except KeyError:
                raise ValueError("Invalid job type provided")

        db.session.commit()
        return applicant


    def delete_applicant(self,applicant_id):
        applicant = Applicants.query.get(applicant_id)
        if not applicant:
            raise ValueError("Applicant not found")

        db.session.delete(applicant)
        db.session.commit()