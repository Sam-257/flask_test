from datetime import datetime
from app import db

# Database class models
class Employees(db.Model):
    employee_id = db.Column(db.Integer, primary_key = True)
    employee_name = db.Column(db.String(20), nullable = False )
    email = db.Column(db.String(120), unique = True, nullable = False)
    #image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable = False)
    leaves = db.relationship('Leaves', backref = 'author',lazy = True)
    #Returning elements of table in the format that we want
    def __repr__(self):
        return f"({self.employee_id},{self.employee_name},{self.email},{self.password})"


class Leaves(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    date_of_leave = db.Column(db.String(10),nullable = False)
    date_posted = db.Column(db.DateTime,nullable = False, default = datetime.utcnow )
    reason = db.Column(db.Text, nullable = False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'),nullable = False)
    status = db.Column(db.Integer, nullable = False)
    def __repr__(self):
        return f"Leaves('{self.id}','{self.date_of_leave}')"

class Admins(db.Model):
    admin_id = db.Column(db.Integer, primary_key = True)
    admin_name = db.Column(db.String(20), nullable = False )
    email = db.Column(db.String(120), unique = True, nullable = False)
    #image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable = False)
    def __repr__(self):
        return f"Employee('{self.admin_id}','{self.admin_name}','{self.email}')"


