"""
This is module supports all the REST actions for querying Transactions data/details.
"""

from sqlalchemy import func
from app_config import db
from datetime import datetime
from models import Transaction

DATE_FORMAT = r'%d %b %y'
REQUEST_DATE_FORMAT = r'%d-%m-%y'

"""
A helper method to convert JSON To Python Objects & save to DB

"""
def db_add(transaction_json):
    withdrawal_amt = transaction_json.get("Withdrawal AMT")
    deposit_amt = transaction_json.get("Deposit AMT")
    balance_amt = transaction_json.get("Balance AMT")

    if withdrawal_amt:
        withdrawal_amt = float(withdrawal_amt.replace(',',''))
    else:
        withdrawal_amt = 0.00
    if deposit_amt:
        deposit_amt = float(deposit_amt.replace(',',''))
    else:
        deposit_amt = 0.00
    if balance_amt:
        balance_amt = float(balance_amt.replace(',',''))
    else:
        balance_amt = 0.00

    # Creating a new Transaction obj
    transaction_obj = Transaction(  
                        account_no=transaction_json.get("Account No"),
                        date=datetime.strptime(transaction_json.get("Date"), DATE_FORMAT),
                        transaction_details=transaction_json.get("Transaction Details"),
                        value_date=datetime.strptime(transaction_json.get("Value Date"), DATE_FORMAT),
                        withdrawal_amt=withdrawal_amt,
                        deposit_amt=deposit_amt,
                        balance_amt=balance_amt,
                    )
    
    # Saving the Transaction to DB
    db.session.add(transaction_obj)
    db.session.commit()
    new_transaction_id = db.session.query(func.max(Transaction.id)).scalar()
    return new_transaction_id  # Returns the new transaction_id


"""
A method to take in transaction details.
from a json string and save it to DB.

:request: A JSON string with the transaction details
:return:  A JSON string as {"id" : "<transaction_id>"}
"""
def withdraw(transaction_json):
  return { "id": "Comming Soon"}, 201

def deposit(transaction_json):
  return { "id": "Comming Soon"}, 201

def check_balance(transaction_json):
    return { "id": "Comming Soon"}, 200

"""
A helper method to serialize a objects' list into
JSON compatible string, i.e Python dict{}
"""
def serialize_objects_list(objs_list):
    dicts_list = []
    for transaction_obj in objs_list:        
        dicts_list.append(serialize_transaction_object(transaction_obj))
    return dicts_list

"""
A helper method to serialize a single object into
JSON compatible string, i.e Python dict{}
"""
def serialize_transaction_object(transaction_obj):
    transactions_dict = {}
    transactions_dict["Id"] = transaction_obj.id
    transactions_dict["Account No"] = transaction_obj.account_no
    transactions_dict["Date"] = transaction_obj.date
    transactions_dict["Transaction Details"] = transaction_obj.transaction_details
    transactions_dict["Value Date"] = transaction_obj.value_date
    transactions_dict["Withdrawal Amt"] = transaction_obj.withdrawal_amt
    transactions_dict["Deposit Amt"] = transaction_obj.deposit_amt
    transactions_dict["Balance Amt"] = transaction_obj.balance_amt

    return transactions_dict


"""
A method (GET) to display all the transaction details.

:return: A JSON list with transaction details from DB
      Eg.
          [{    "id": 1,
                "Account No": 409000611074,
                "Date": "5 Jul 17",
                "Transaction Details": "TRF FROM  Indiaforensic SERVICES",
                "Value Date": "5 Jul 17",
                "Withdrawal AMT": "",
                "Deposit AMT": "10,00,000.00",
                "Balance AMT": "20,00,000.00"
            },
            .
            .
            .
          ]
"""
def list_transactions(_limit=None):
  transaction_objs_list = db.session.query(Transaction).order_by(Transaction.id).limit(_limit).all()
  return serialize_objects_list(transaction_objs_list)


def get_all_transactions_by_date(search_date):
    date = datetime.strptime(search_date, REQUEST_DATE_FORMAT)
    transaction_objs_list = Transaction.query.filter(Transaction.date == date)
    return serialize_objects_list(transaction_objs_list)



"""
A helper method to check if a transaction exists in DB or not.
:return: transaction_obj if exists, else an error message
"""
def does_transaction_exists(transaction_id):
  transaction_obj = Transaction.query.filter(Transaction.id == transaction_id).one_or_none()
  if transaction_obj is None:
    error_message = f'transactionId {transaction_id} does not exits.'
    return error_message
  else:
    return transaction_obj



def get_single_transaction_by_id(transaction_id):
    try: 
        transaction_id = int(transaction_id)
    except ValueError as ve:
        return {"message": "transactionId should be numeric."}, 400

    transaction_obj = does_transaction_exists(transaction_id)
    if isinstance(transaction_obj, Transaction):
        return serialize_transaction_object(transaction_obj)
    else:
        return {"message" : transaction_obj}, 404


def add_new_transaction(transaction_json):
    new_transaction_id = db_add(transaction_json)
    transaction_obj = db.session.query(Transaction).get(new_transaction_id)
    if isinstance(transaction_obj, Transaction):
        return serialize_transaction_object(transaction_obj)
    else:
        return {"message" : transaction_obj}, 404