from mongoengine import connect
from lib.setup.setup import *
from dotenv import load_dotenv, find_dotenv, get_key

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)
if( get_key(dotenv_file, "MONGODB_DATABASE") == None or get_key(dotenv_file, "MONGODB_USERNAME") == None):
    check()
db_name = get_key(dotenv_file, "MONGODB_DATABASE")
db_user = get_key(dotenv_file, "MONGODB_USERNAME")
db_pass = get_key(dotenv_file, "MONGODB_PASSWORD")

def connect_db():
    db = connect(
        db=db_name,
        username=db_user,
        password=db_pass,
        host='mongodb://'+db_user+':'+db_pass+'@localhost/'+db_name
    )
    return db
