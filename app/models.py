from app import db


class Employee(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),unique=True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    bio = db.Column(db.String(1000))
    blog = db.relationship('Blog', backref = "employee")
    

    def __repr__(self):
        return f"{self.username} first_name:{self.first_name} last_name:{self.last_name}"

class Blog(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title =  db.Column(db.String(40))
    content =  db.Column(db.String(500))
    employee_id = db.Column(db.Integer,db.ForeignKey('employee.id'))


class Projects(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(500))
    #Remember to add the image file link