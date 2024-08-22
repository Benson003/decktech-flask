from models import models
from app import db
import bcrypt
class User():

    def get_all_users(self):
        models.User.query.all()


    def get_specfic_user(self,id):
        models.User.query.filter(models.User.id == id)

    
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
    pass

class Projects():
    def read_all_projects(self):
        models.Projects.query.all()

    def read_spefic_project(self,id):
        models.Projects.query.filter(models.Projects.id == id)

    def create_project(self,title,content):
        project = models.Projects(title=title,content=content)

        db.session.add(project)
        db.session.commit()