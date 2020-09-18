import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Model creation
class Puppy(db.Model):
    # Table
    __tablename__ = 'puppies'  # overwrite table name (default from class name+s)

    # Columns:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    # Define the class methods
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # STR Representation
    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old."
