import json
from cerberus import Validator
from food_expense_tracker import db
from food_expense_tracker import app
from food_expense_tracker.models import ExpenseLog
from food_expense_tracker.models import User, Account

from flask import request, jsonify
from flask_jwt_extended import (
     jwt_required, create_access_token, create_refresh_token,
    get_jwt_identity
)

@app.route('/api/login', methods = ['POST'])
def login():
    json_request_data = request.get_json()
    schema = {
        'username': { 'type': 'string', 'required': True, 'empty': False},
        'password': {'type': 'string', 'required': True, 'empty': False}
    }
    
    validator = Validator(schema)
    isValidRequest = validator.validate(request.json)
    if not isValidRequest:
        return jsonify(validator.errors)
    username = json_request_data.get('username')
    username = username.lower()
    
    login_user = User.query.filter_by(username=username).first() 
    if not login_user:
        return jsonify(login_error="Invalid login"), 400

    password = json_request_data.get('password')

    if password == login_user.password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(login_error="Invalid login"), 400


# Protect a view with jwt_required, which requires a valid access token
# in the request to access.
@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


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
    
    user_account = Account.query.filter_by(email=email).first()
    user = User()
    user.email = email
    user.username = username
    user.password = password
    user.account_id = user_account.id

    db.session.add(user)
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

@app.route("/debug_connect", methods=['GET'])
def debug_connect():
    import ptvsd
    ptvsd.enable_attach(address=("0.0.0.0", 5678))
    ptvsd.wait_for_attach()
    return "True" 
