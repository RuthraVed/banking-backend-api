from app_config import db
from sqlalchemy import func


class Transaction(db.Model):
    __tablename__ = "transactions"
    id = db.Column(db.Integer, primary_key=True)
    account_no = db.Column(db.BigInteger, nullable=False)
    date = db.Column(db.DateTime, nullable=False, server_default=func.now()) 
    transaction_details = db.Column(db.String(128))
    value_date = db.Column(db.DateTime, nullable=False, server_default=func.now())
    withdrawal_amt = db.Column(db.Float(precision=12, decimal_return_scale=2), nullable=True)
    deposit_amt = db.Column(db.Float(precision=12, decimal_return_scale=2), nullable=True)
    balance_amt = db.Column(db.Float(precision=12, decimal_return_scale=2))
