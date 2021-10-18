from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from datetime import timedelta


app = Flask(__name__)
app.config['SECRET_KEY'] = '25b720ef729a53baf9030f28fd179129'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.permanent_session_lifetime = timedelta(days=5)

# Database stuff
db = SQLAlchemy(app)

from flaskblog import routes
