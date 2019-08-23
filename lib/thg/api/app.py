from flask import Flask, request
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine
from lib.thg.core.Database.Connection import *

from mongoengine import connect
from lib.setup.setup import *
from dotenv import load_dotenv, find_dotenv, get_key, dotenv_values
from lib.thg.rootpath import ROOT_PATH

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)
client = docker.from_env()

file_db_creds = dotenv_values(dotenv_file)
dbcreds = {"MONGODB_DATABASE", "MONGODB_USERNAME", "MONGODB_PASSWORD"}
db_name = get_key(dotenv_file, "MONGODB_DATABASE")
db_user = get_key(dotenv_file, "MONGODB_USERNAME")
db_pass = get_key(dotenv_file, "MONGODB_PASSWORD")
    #db = connect(db=db_name,username=db_user,password=db_pass,host='mongodb://'+db_user+':'+db_pass+'@localhost/'+db_name)



app = Flask(__name__)
api = Api(app)
app.config['MONGODB_SETTINGS'] = {
    'db': db_name,
    'host': '127.0.0.1',
    'port': 27017
    ''
}
todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)