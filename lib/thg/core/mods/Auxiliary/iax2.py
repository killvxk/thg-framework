from lib.thg.base.BaseOptions import BaseOption
from lib.thg.base.BaseOptions import BaseOptions
from lib.thg.base.BaseResult import BaseResult

class BaseAuxiliary_iax2:
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



    def register_iax2(self, timeout_value=5, threads_value=1):
        self.target_type = "http"
        self.register_options([
          BaseOption(name='IAX_HOST', required=True, description='The IAX2 server to communicate with'),
          BaseOption(name='IAX_PORT', required=True, description='The IAX2 server port', value=4569),
          BaseOption(name='IAX_USER', required=False, description='An optional IAX2 username'),
          BaseOption(name='IAX_PASS', required=False, description='An optional IAX2 password', value=""),
          BaseOption(name='IAX_CID_NAME', required=False, description='The default caller ID name', value=''),
          BaseOption(name='IAX_CID_NUMBER', required=True, description='The default caller ID number',value='15555555555'),
          BaseOption(name='IAX_DEBUG', required=False, description='Enable IAX2 debugging messages', value=False)
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






