from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from food_expense_tracker import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI 

db = SQLAlchemy(app)
""" SQLAlchemy """


from food_expense_tracker import routes, models