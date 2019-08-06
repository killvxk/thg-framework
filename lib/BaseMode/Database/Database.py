#conexao com o banco de dados
import mongoengine, dotenv, os
from lib.BaseMode.Database import Connection
from lib.BaseMode.Database import Models
from lib.setup import setup
#from fnmatch import fnmatchcase
#from utils.files import ROOT_PATH
#from utils.module import name_convert
#from importlib import import_module

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

class Database:
    searchable_fields = ['name', 'module_name', 'description', 'author',
                         'disclosure_date', 'service_name', 'service_version',
                         'check', 'rank']

    def __init__(self):
        self.connection = Connection.connect_db()

    def get_module_count(self):
        count = Models.mod_refs.objects.all().count()
        return count

    def insert_module(self, info):
        module = Models.mod_refs(module = info['module'], mtype = info['mtype'], ref = info['ref'])
        module.save()

    def db_rebuild(self):
        print("Rebuilding Database..")
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
        return Models.mod_refs.objects.all()

    def search_modules(self, search_conditions):
        name = search_conditions.get('name', '')
        module_name = search_conditions.get('module_name', '')
        description = search_conditions.get('description', '')
        author = search_conditions.get('author', '')
        disclosure_date = search_conditions.get('disclosure_date', '')
        service_name = search_conditions.get('service_name', '')
        service_version = search_conditions.get('service_version', '')
        check = search_conditions.get('check', '')
