from lib.thg.base.BaseOptions import BaseOption
from lib.thg.base.BaseOptions import BaseOptions
from lib.thg.base.BaseResult import BaseResult

class BaseAuxiliary_Udp_Scanner:
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

    def register_udp_scanner(self, timeout_value=5, threads_value=1):
      self.target_type = "http"
      self.register_options([
            BaseOption(name='BATCHSIZE', required=True, description='The number of hosts to probe in each set', value=256),
            BaseOption(name='THREADS',  required=True, description="The number of concurrent threads", value=10),
            #Opt::CHOST,
            #Opt::CPORT,
            BaseOption(name='ScannerRecvInterval',  required=True, description='The maximum numbers of sends before entering the processing loop', value=30),
            BaseOption(name='ScannerMaxResends',  required=True, description='The maximum times to resend a packet when out of buffers', value=10),
            BaseOption(name='ScannerRecvQueueLimit',  required=True, description='The maximum queue size before breaking out of the processing loop', value=100),
            BaseOption(name='ScannerRecvWindow',  required=True, description='The number of seconds to wait post-scan to catch leftover replies', value=15)
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

