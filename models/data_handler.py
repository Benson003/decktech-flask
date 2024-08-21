from models import models
from app import db
import bcrypt
class User():

    def get_all_users():
        models.User.query.all()


    def get_specfic_user(id):
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