from lib.thg.base.BaseOptions import BaseOption
from lib.thg.base.BaseOptions import BaseOptions
from lib.thg.base.BaseResult import BaseResult

class BaseAuxiliary_Sms:
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
    def register_Sms(self, timeout_value=5, threads_value=1):
      self.target_type = "http"
      self.register_options([
            BaseOption(name='RUNTIME',required=True, description="The number of seconds to run the test", value=5),
            BaseOption(name='SMTPFROM', required=False, description='The FROM field for SMTP', volue=''),
            BaseOption(name='SMTPADDRESS', required=True, description='The SMTP server to use to send the text messages', volue=""),
            BaseOption(name='SMTPPORT', required=True, description='The SMTP port to use to send the text messages',value=25),
            BaseOption(name='SMTPUSERNAME', required=True,description='The SMTP account to use to send the text messages'),
            BaseOption(name='SMTPPASSWORD', required=True, description='The SMTP password to use to send the text messages',value=''),
            BaseOption(name='SMSCARRIER', required=True, description='The targeted SMS service provider', volue=""),
            BaseOption(name='CELLNUMBERS', required=True, description='The phone numbers to send to', volue=""),
            BaseOption(name='SMSMESSAGE', required=True, description='The text message to send', volue=""),
            BaseOption(name='SMSSUBJECT', required=False, description='The text subject', volue=""),
            BaseOption(name='SmtpLoginType', required=True, description='The SMTP login type'),
            BaseOption(name='HeloDdomain', required=False, description='The domain to use for HELO', volue='')
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



