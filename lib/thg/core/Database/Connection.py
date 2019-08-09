from mongoengine import connect
from lib.setup.setup import *
from dotenv import load_dotenv, find_dotenv, get_key, dotenv_values
from lib.thg.rootpath import ROOT_PATH

try:
    import docker
except ImportError:
    check()

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)
client = docker.from_env()

def connect_db():
    try:
        client.containers.get("thgdb-mongodb").start()
    except:
        check()
    file_db_creds = dotenv_values(dotenv_file)
    dbcreds = {"MONGODB_DATABASE", "MONGODB_USERNAME", "MONGODB_PASSWORD"}
    if( file_db_creds  == {} or not ( file_db_creds.keys() >= dbcreds) ):
        check()

    db_name = get_key(dotenv_file, "MONGODB_DATABASE")
    db_user = get_key(dotenv_file, "MONGODB_USERNAME")
    db_pass = get_key(dotenv_file, "MONGODB_PASSWORD")
    db = connect(
        db=db_name,
        username=db_user,
        password=db_pass,
        host='mongodb://'+db_user+':'+db_pass+'@localhost/'+db_name
    )

    return db
