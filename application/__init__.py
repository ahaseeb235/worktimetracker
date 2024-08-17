from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'pa55word'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///worktimeDB.db'


db = SQLAlchemy(app)
app.app_context().push() # adding context

from application import routes