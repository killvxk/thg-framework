#conexao com o banco de dados
#from sqlalchemy import create_engine
#import psycopg2
import mongoengine
import dotenv
from lib.BaseMode.Database.Connection import connect_db
from lib.BaseMode.Database import Models
import setup
#import Connection, Models
import os
import sqlite3
from fnmatch import fnmatchcase
from utils.files import ROOT_PATH
from utils.module import name_convert
from importlib import import_module

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

class Database:

    connection = None
    cursor = None
    searchable_fields = ['name', 'module_name', 'description', 'author', 'disclosure_date', 'service_name', 'service_version', 'check', 'rank']

    def __init__(self):
        #self.insert_module(self, {"module": "Module 4 Teste", "mtype": "Tipo 4", "ref": "asdasasdasdasd"})
        #self.get_module_count(self)
        print(Models.mod_refs())
        #self.create_table()
        #if self.get_module_count() == 0:
        #    self.db_rebuild()

    #def get_module_count(self):
        #count =
        #print(count)

    def insert_module(self, info):
        module = Models.mod_refs(module = info['module'], mtype = info['mtype'], ref = info['ref'])
        module.save()

    def db_rebuild(self):
        #
        setup.check()

        """for directory_name, directories, filenames in os.walk('modules/'):
            for filename in filenames:
                if filename not in ['__init__.py']\
                        and not fnmatchcase(filename, "*.pyc")\
                        and fnmatchcase(filename, "*.py"):
                    full_name = "{directory}/{filename}".format(directory=directory_name, filename=filename)
                    module_name = name_convert(full_name)
                    module_class = import_module("modules.{module_name}".format(
                        module_name=module_name.replace("/", ".")
                    ))
                    module_instance = module_class.Modules()
                    module_info = module_instance.get_info()
                    module_info['module_name'] = module_name
                    try:
                        getattr(module_instance, 'check')
                        module_info['check'] = 'True'
                    except AttributeError:
                        module_info['check'] = 'False'
                    self.insert_module(module_info)"""

    def get_modules(self):
        sql = "select `module_name`, `check`, `disclosure_date`, `description` from modules;"
        rs = self.cursor.execute(sql)
        return rs.fetchall()

    def search_modules(self, search_conditions):
        name = search_conditions.get('name', '')
        module_name = search_conditions.get('module_name', '')
        description = search_conditions.get('description', '')
        author = search_conditions.get('author', '')
        disclosure_date = search_conditions.get('disclosure_date', '')
        service_name = search_conditions.get('service_name', '')
        service_version = search_conditions.get('service_version', '')
        check = search_conditions.get('check', '')
        sql = (
            'select `module_name`, `check`, `disclosure_date`, `description` from modules where '
            '`name` like "%{name}%" '
            'and `module_name` like "%{module_name}%" '
            'and `description` like "%{description}%" '
            'and `author` like "%{author}%" '
            'and `disclosure_date` like "%{disclosure_date}%" '
            'and `service_name` like "%{service_name}%" '
            'and `service_version` like "%{service_version}%" '
            'and `check` like "%{check}%" ;'
        ).format(
            name=name,
            module_name=module_name,
            description=description,
            author=author,
            disclosure_date=disclosure_date,
            service_name=service_name,
            service_version=service_version,
            check=check
        )
        rs = self.cursor.execute(sql)
        return rs.fetchall()

#Database.__init__(Database)
