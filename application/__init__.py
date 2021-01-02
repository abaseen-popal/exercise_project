from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")
app.config['SECRET_KEY'] = "dhfihafihsfihdsidfhsi"
db = SQLAlchemy(app)

from application import routes