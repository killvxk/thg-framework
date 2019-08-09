from lib.thg.base.BaseOptions import BaseOption
from lib.thg.base.BaseOptions import BaseOptions
from lib.thg.base.BaseResult import BaseResult

class BaseAuxiliary_Llmnr:
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

    def register_Llmnr(self, timeout_value=5, threads_value=1):
      self.target_type = "http"
      self.register_options([
        BaseOption(name="RHOST", required=True, description="ip to test"),
        BaseOption(name="RHOST", required=True, description="ip to test"),
        BaseOption(name='RHOSTS', required=False, description='The multicast address or CIDR range of targets to query',value='224.0.0.252'),
        BaseOption(name='RPORT', required=False, description="port of connection", value=5355),
        BaseOption(name='NAME', required=True, description='The name to query', volue='localhost'),
        BaseOption(name='TYPE', required=True, description='The query type (name, # or TYPE#)', value='A')
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








