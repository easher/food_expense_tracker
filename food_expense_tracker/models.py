import datetime
from food_expense_tracker import config
from food_expense_tracker import db
from sqlalchemy_utils import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(EncryptedType(db.String, config.SECRET_AES_KEY, AesEngine, 'pkcs5'))
    
class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True, nullable=False)


class ExpenseLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expense_name = db.Column(db.String(60), unique=False, nullable=False)
    expense_type = db.Column(db.Integer, nullable=False)
    expense_cost = db.Column(db.BigInteger)
    expense_time_utc = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)


