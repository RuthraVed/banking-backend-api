import json
from pathlib import Path
from app_config import db
from resources import transaction_resource

CURRENT_DIR = Path.cwd()

DB_DIR = CURRENT_DIR / 'db'

# A condition to create a folder if not exists,
# and if already exists, doesn't raise any FileExistsError
DB_DIR.mkdir(parents=True, exist_ok=True)

SQLITE_DB_FILE = DB_DIR / 'banking_api.db'
DATA_FILES = CURRENT_DIR / 'data_files/'


def db_remove_old():
    # Delete database file if it exists currently
    SQLITE_DB_FILE.unlink(missing_ok=True)

    # Create the database
    db.create_all()


# ----------------ADDING GIVEN TRANSACTIONS------------------------------------------
def load_transactions_to_db():

    # Reading from the given bankAccountdde24ad.json file
    with open(DATA_FILES / "bankAccountdde24ad.json", "r") as json_file:
        transactions = json.load(json_file)

    for transaction_detail in transactions:
        # Using the method transaction_resource.add_transaction()
        print(transaction_resource.db_add(transaction_detail))
        
    print("\tINFO: Transactions' table created.")



#---------------------MAIN-------------------------------------------------------------------
def db_initialize():
    db_remove_old()
    load_transactions_to_db()
    print("\tINFO: Successful DB initialization")


db_initialize()
