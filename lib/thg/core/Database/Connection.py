from mongoengine import connect
from lib.setup.setup import GenerateDotEnv, HashGen
from dotenv import load_dotenv, find_dotenv, get_key

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)
try:
    db_name = get_key(dotenv_file, "MONGODB_DATABASE")
    db_user = get_key(dotenv_file, "MONGODB_USERNAME")
    db_pass = get_key(dotenv_file, "MONGODB_PASSWORD")
except:
    GenerateDotEnv()
    db_name = dotenv.set_key(dotenv_file, "MONGODB_DATABASE", "thgdb")
    db_user = dotenv.set_key(dotenv_file, "MONGODB_USERNAME", "thguser")
    db_pass = HashGen()

def connect_db():
    db = connect(
        db=db_name,
        username=db_user,
        password=db_pass,
        host='mongodb://'+db_user+':'+db_pass+'@localhost/'+db_name
    )
    return db
