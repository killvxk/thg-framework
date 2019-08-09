#conexao com o banco de dados
import mongoengine, dotenv, os, json
from lib.thg.core.Database import Connection, DBGen
from lib.thg.core.Database import Models
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
        #self.insert_module(self, {'module': "Module4",'mtype': "payload", 'ref': 'sdasdasdasdas'})

    def get_module_count(self):
        count = Models.mod_refs.objects.all().count()
        return count

    def insert_module(self, info):
        module = Models.mod_refs(module = info['module'], mtype = info['mtype'], ref = info['ref'])
        module.save()

    def db_rebuild(self):
        print("Rebuilding Database..")
        setup.check()
        mongoengine.disconnect(alias="default")
        self.connection = Connection.connect_db()
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
        return Models.module_details.objects.all()
    """def get_modules(self):
        return Models.mod_refs.objects.all()"""

    def load_modules():
        return DBGen.module.get_local_modules()

    def search_modules(self, search):
        #name = search_conditions.get('name', '')
        #valid_args = ['module_name', 'description', 'author', 'disclosure_date',
        #                 'service_name', 'service_version', 'check']
        #self.validate_search(search['module_name'])
        modules = []
        query = json.loads(Models.mod_refs.objects(module__icontains=search).to_json())
        #q2 = load_modules()
        #q2 = json.loads(Models.module_details.objects().to_json())
        #print(type(q2))
        #must have [ module_mixins, module_name, module_type, module_info,
        #           module_archs, module_authors, module_details, module_class ]
        if(query == []):
            return query
        """module_name = search.get('module_name', '')
        description = search.get('description', '')
        author = search.get('author', '')
        disclosure_date = search.get('disclosure_date', '')
        service_name = search.get('service_name', '')
        service_version = search.get('service_version', '')
        check = search.get('check', '')"""
        for q in query:
            q.pop('_id')
            modules.append(q)
        keys = modules[0].keys()
        m_values =[[row[key] for key in keys] for row in modules]
        #print(m_values)
        return [m_values, list(keys)]

    #def validate_search(self, search):
    #    #
    #    print(search)
