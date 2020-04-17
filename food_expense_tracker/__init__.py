from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from food_expense_tracker import config

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI 
db = SQLAlchemy(app)

app.config['JWT_SECRET_KEY'] = config.JWT_SECRET_KEY
jwt = JWTManager(app)


from food_expense_tracker import routes, models