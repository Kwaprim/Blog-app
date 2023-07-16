from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)

app.config['SECRET_KEY'] = '6a7bd560cad038cea4053de73c5cf6f5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes