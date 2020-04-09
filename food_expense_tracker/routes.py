from food_expense_tracker import db
from food_expense_tracker import app
@app.route("/")
def index():
    return "Hello from Flask!"

@app.route("/gen_db")
def gen_db():
    db.create_all()
    return "omg"