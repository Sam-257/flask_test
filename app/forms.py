#Forms in Flask
from flask_wtf import FlaskForm
#importing datatypes
from wtforms import StringField, PasswordField, SubmitField, BooleanField
#importing form validators
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    employee_name = StringField('Name', validators = [DataRequired(), Length(min = 2,max = 20)])
    email = StringField('Email',validators = [DataRequired(), Email(), Length(min = 2,max = 20)])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 2,max = 20)])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email',validators = [DataRequired(), Email(), Length(min = 2,max = 20)])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 2,max = 20)])
    submit = SubmitField('Login')
