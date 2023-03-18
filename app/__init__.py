from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)                   #creating Flask instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///axiomio.db'     #Setting AQLAlchemy URI, sql or mysql can be selected
app.config['SECRET_KEY'] = 'a83b1cefe5a5c6f8745ecf902'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    #used for signal limiting
#URI --- Uniform Resource Identifier
db = SQLAlchemy(app)                    #creating database instance...we'll later call db models

from app import routes