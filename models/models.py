from app import db
from sqlalchemy import Enum
import enum


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),unique=True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    password = db.Column(db.String(256))
    bio = db.Column(db.String(256))
    blog = db.relationship('Blog', backref = "user")


    def __init__(self,username,first_name,last_name,bio,password=None):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.bio = bio
        self.password = password

    def __repr__(self):
        return f"{self.username} first_name:{self.first_name} last_name:{self.last_name}"

class Blog(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title =  db.Column(db.String(40))
    content =  db.Column(db.String(500))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __init__(self,title,content,user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f"id:{ self.id }Blog Post:{ self.title }"

class Projects(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(500))

    #Remember to add the image file link

    def __init__(self, title,content):
        self.title = title
        self.content = content

    def __repr__(self):
        return f"id:{self.id} , title:{self.title} ,content:{self.content}"
    

class JobType(enum.Enum):

    INTERNSHIP = "Internship"
    ON_SITE = "On-Site"
    REMOTE = "Remote"
    HYBRID = "Hybrid"
    OTHERS = "Others"

class Applicants(db.Model):

    id = db.Column(db.Integer,primary_key = True)
    fullname = db.Column(db.String(200))
    role = db.Column(Enum(JobType))

    def __init__(self,fullname,role):
        self.fullname = fullname
        self.role = role

    def __repr__(self):
        return f"Fullname: {self.fullname} , Role:{self.role} "
    