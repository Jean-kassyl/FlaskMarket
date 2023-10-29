from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db"
app.config['SECRET_KEY'] = '7aa4b18d9a6ed29d8b2937e6'
db = SQLAlchemy(app)
app.app_context().push()

from market import routes

