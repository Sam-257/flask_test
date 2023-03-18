from flask import Flask,render_template, url_for, request, redirect
#We are using "render_template" to render a file from templates folder
from app.forms import RegistrationForm, LoginForm
from app import app
from app.models import Employees, Leaves, Admins
from app import db

'''testtable= [
    {"employee_id": 1, "employee_name": "Shinchan", "email": "shinchan@shero.com"},
    {"employee_id": 2, "employee_name": "Sam", "email": "sam@shero.com"},
    {"employee_id": 3, "employee_name": "Pam", "email": "pam@shero.com"},
    {"employee_id": 4, "employee_name": "Tom", "email": "tom@shero.com"},
    {"employee_id": 5, "employee_name": "Tim", "email": "tim@shero.com"}
]'''
#--------------------Queries---------------------

allEmployees = Employees.query.all()
allAdmins = Admins.query.all()
print(allEmployees)
# -------------employee-----------
@app.route('/',methods = ['GET','POST'])                                 #index or login page
@app.route('/index',methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_email = Employees.query.filter_by(email = form.email.data).first()
        if db_email:
            if db_email.password == form.password.data:
                return redirect(url_for('dashboard'))
        admin_email = Admins.query.filter_by(email = form.email.data).first()
        if admin_email:
            if admin_email.password == form.password.data:
                return redirect(url_for('adminDashboard'))
        
            
        return render_template('index.html', title = "Login",form = form, place = "Invalid email or password")
    return render_template('index.html', title = "Login",form = form, place ="")

'''@app.route('/login_check',methods = ['GET','POST'])
def login_check():
#    form = LoginForm()
    email_check = request.form['email']
    password_check = request.form['password']
    

    if email_check in allEmployees.email and password_check in allEmployees.password:
        return redirect(url_for('dashboard'))
    
    elif email_check in allAdmins.email and password_check in allAdmins.password:
        return redirect(url_for('adminDashboard'))

    else:
        return render_template('index.html', title = "Login")

'''
    
@app.route('/dashboard')                        #Dashboard
def dashboard():
    return render_template('dashboard.html', title = "Dashboard") 

@app.route('/applyForLeave')                    #Apply for leave
def applyForLeave():
    return render_template('applyForLeave.html') 

@app.route('/statusOfLeave')                    #Status of leave
def statusOfLeave():
    return render_template('statusOfLeave.html') 

@app.route('/registerEmployee',methods = ['GET','POST'])                    #Register Employee
def registerEmployee():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_employee = Employees(employee_name = form.employee_name.data, email = form.email.data, password = form.password.data)
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('registerEmployee.html', title = "Register", form = form) 

@app.route('/siteLayout')                    #Site Layout
def siteLayout():
    return render_template('siteLayout.html') 


#-----------------employer------------
'''@app.route('/admin/login')                    #Admin Login
@app.route('/admin/')                    #Admin Login
def adminLogin():
    return render_template('adminLogin.html') 
'''
@app.route('/admin/dashboard')                    #Admin Login
def adminDashboard():
    return render_template('admin/adminDashboard.html', title = "Dashboard") 

@app.route('/admin/employeesList')                    #Admin Login
def employeesList():
    
    return render_template('admin/employeesList.html',title = "Employee List", elements = allEmployees) 

