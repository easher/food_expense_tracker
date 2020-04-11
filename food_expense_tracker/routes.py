import json
from food_expense_tracker import db
from food_expense_tracker import app
from food_expense_tracker.models import ExpenseLog


from flask import request, jsonify


@app.route("/")
def index():
    return "Hello from Flask!"

@app.route("/gen_db")
def gen_db():
    db.drop_all()
    db.create_all()
    return "Database destroyed and rebuilt"


@app.route("/log_expense", methods=['POST'])
def log_expense():
    # {
    #     "title" => "Expense name"
    #     "type" =>  "expense type. see ExpenseLogHelper for valid types"
    #     "price" => numeric
    #     "receipt" => "Encoded Image"
    #     "datetime" => "optional"
    # }
    posted_json = jsonify(request.json)
    return posted_json

#def validate_expense_log_request()