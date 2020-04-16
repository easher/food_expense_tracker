import json
from cerberus import Validator
from food_expense_tracker import db
from food_expense_tracker import app
from food_expense_tracker.models import ExpenseLog
from food_expense_tracker.models import User, Account


from flask import request, jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

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
    
    password = json_request_data.get('password')
    username = json_request_data.get('username')
    # check that password matches username
    # if not, return 400
    
    if password != 'password':
        return jsonify({"msg": "incorrect password"}), 400

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


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