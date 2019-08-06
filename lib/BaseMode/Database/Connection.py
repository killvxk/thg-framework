import mongoengine
import dotenv

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

db_name = dotenv.get_key(dotenv_file, "MONGODB_DATABASE")
db_user = dotenv.get_key(dotenv_file, "MONGODB_USERNAME")
db_pass = dotenv.get_key(dotenv_file, "MONGODB_PASSWORD")

def connect_db():
    db = mongoengine.connect(
        db=db_name,
        username=db_user,
        password=db_pass,
        host='mongodb://'+db_user+':'+db_pass+'@localhost/'+db_name
    )
    return db
