import json
from cerberus import Validator
from food_expense_tracker import db
from food_expense_tracker import app
from food_expense_tracker.models import ExpenseLog
from food_expense_tracker.models import User, Account


from flask import request, jsonify


@app.route('/api/users', methods = ['POST'])
def new_user():
    json_request_data = request.get_json()
    schema = {
        'username': { 'type': 'string', 'required': True, 'empty': False},
        'email' :  {'type': 'string', 'required': True, 'empty': False},
        'password': {'type': 'string', 'required': True, 'empty': False}
    }
    
    validator = Validator(schema)
    isValidRequest = validator.validate(request.json)
    if not isValidRequest:
        return jsonify(validator.errors)

    
    username = json_request_data.get('username')
    password = json_request_data.get('password')
    email = json_request_data.get('email')
    
    username = username.lower()
    email = email.lower()

    doesUsernameExist = User.query.filter_by(username=username).first(); 
    if doesUsernameExist:
        return "there already exists a user with that username"
    
    doesEmailExist = User.query.filter_by(email=email).first(); 
    if doesUsernameExist:
        return "there already exists a user with that username"
    
    doesAccountExist =Account.query.filter_by(email=email).first(); 
    if doesAccountExist:
        return "there already exists an account with that email"
    
    
    # create and save account
    account = Account()
    account.email = email
    db.session.add(account)
    db.session.commit()
    
    user_account = Account.query.filter_by(email=email)
    user = User()
    user.email = email
    user.username = username
    user.password = password
    user.account = user_account
    db.session.commit()

    return user.username

@app.route("/")
def index():
    return "Hello fromFlask!"

@app.route("/gen_db")
def gen_db():
    db.drop_all()
    db.create_all()
    return "Database destroyed and rebuilt"


@app.route("/log_expense", methods=['POST'])
def log_expense():
    posted_json = jsonify(request.json)
    return posted_json