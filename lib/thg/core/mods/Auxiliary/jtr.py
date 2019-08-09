from lib.thg.base.BaseOptions import BaseOption
from lib.thg.base.BaseOptions import BaseOptions
from lib.thg.base.BaseResult import BaseResult

class BaseAuxiliary_JTR:
    name = None #nome do auxiliar
    description = None #descricao do auxiliar
    author = [] # nome do autor
    references = []#referenia do exploit
    disclosure_date = None #data de divulgacao
    service_name = None #nome do servico
    service_version = None #versao do servico
    dbinfo = ['name', 'description', 'author', 'references', 'disclosure_date', 'service_name', 'service_version']#info database
    multi_target = False#vvarios alvos
    targets = []#alvo
    target_type = None#tipo de alvo
    options = None #opcoes
    results = None #resultados

    def __init__(self):
        self.multi_target = False
        self.target_type = None
        self.targets = []
        self.options = BaseOptions()
        self.results = BaseResult()

    def get_info(self):
        info = {}
        for field_name in self.dbinfo:
            info[field_name] = getattr(self, field_name)
        return info


    def register_JTR(self, timeout_value=5, threads_value=1):
        self.target_type = "http"

        self.register_options([
            BaseOption(name='CONFIG', required=True,
                       description='The path to a John config file to use instead of the default'),
            BaseOption(name='CUSTOM_WORDLIST', required=True, description='The path to an optional custom wordlist'),
            BaseOption(name='ITERATION_TIMEOUT', required=True,
                       description='The max-run-time for each iteration of cracking'),
            BaseOption(name='JOHN_PATH', required=True,
                       description='The absolute path to the John the Ripper executable'),
            BaseOption(name='KORELOGIC', required=True,
                       description='Apply the KoreLogic rules to Wordlist Mode(slower)', value=False),
            BaseOption(name='MUTATE', required=True, description='Apply common mutations to the Wordlist (SLOW)',
                       value=False),
            BaseOption(name='POT', required=True,
                       description='The path to a John POT file to use instead of the default'),
            BaseOption(name='USE_CREDS', required=True,
                       description='Use existing credential data saved in the database', value=True),
            BaseOption(name='USE_DB_INFO', required=True,
                       description='Use looted database schema info to seed the wordlist', value=True),
            BaseOption(name='USE_DEFAULT_WORDLIST', required=True, description='Use the default metasploit wordlist',
                       value=True),
            BaseOption(name='USE_HOSTNAMES', required=True,
                       description='Seed the wordlist with hostnames from the workspace', value=True),
            BaseOption(name='USE_ROOT_WORDS', required=True, description='Use the Common Root Words Wordlist',
                       value=True),
            BaseOption(name='DeleteTempFiles', required=True, description='Delete temporary wordlist and hash files',
                       value=True)
        ])

    def thg_update_info(self, info):
        for name in info:
            if name in self.dbinfo:
                setattr(self, name, info[name])

    def register_options(self, option_array):
        for option in option_array:
            self.options.add_option(option)

    def get_missing_options(self):
        def is_missing(option):
            return option.required and option.value in [None, '']

        missing_options = filter(is_missing, self.options.get_options())
        return list(missing_options)



