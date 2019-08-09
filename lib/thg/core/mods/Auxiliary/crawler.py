from lib.thg.base.BaseOptions import BaseOption
from lib.thg.base.BaseOptions import BaseOptions
from lib.thg.base.BaseResult import BaseResult

class BaseAuxiliary_Crawler:
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

    def register_crawler(self):
      self.target_type = "http"
      self.register_options([
        BaseOption(name="RHOST", required=True, description="ip to test"),
        BaseOption(name="RPORT", required=True, description="port", value=80),
        BaseOption(name='VHOST', required=False, description="HTTP server virtual host"),
        BaseOption(name='URI', required=True, description="The starting page to crawl", value="/"),
        BaseOption(name="Proxies", required=True, description="proxy to connnect"),
        BaseOption(name='MAX_PAGES', required=True, description='The maximum number of pages to crawl per URL',value=500),
        BaseOption(name='MAX_MINUTES', required=True, description='The maximum number of minutes to spend on each URL',value=5),
        BaseOption(name='MAX_THREADS', required=True, description='The maximum number of concurrent requests', value=4),
        BaseOption(name='HttpUsername', required=False, description='The HTTP username to specify for authentication'),
        BaseOption(name='HttpPassword', required=False, description='The HTTP password to specify for authentication'),
        BaseOption(name='DOMAIN', required=True, description='The domain to use for windows authentication',value='WORKSTATION'),
        BaseOption(name='SSL', required=False, description='Negotiate SSL/TLS for outgoing connections', value=False),
        BaseOption(name='DirBust', required=False, description='Bruteforce common URL paths', value=True),
        BaseOption(name='RequestTimeout', required=False,description='The maximum number of seconds to wait for a reply', value=15),
        BaseOption(name='RedirectLimit', required=False,description='The maximum number of redirects for a single request', value=5),
        BaseOption(name='RetryLimit', required=False, description='The maximum number of attempts for a single request',value=5),
        BaseOption(name='UserAgent', required=True, description='The User-Agent header to use for all requests',value="Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        BaseOption(name='BasicAuthUser', required=False,description='The HTTP username to specify for basic authentication'),
        BaseOption(name='BasicAuthPass', required=False,description='The HTTP password to specify for basic authentication'),
        BaseOption(name='HTTPAdditionalHeaders', required=False,description="A list of additional headers to send (separated by \\x01)"),
        BaseOption(name='HTTPCookie', required=False, description="A HTTP cookie header to send with each request"),
        BaseOption(name='SSLVersion', required=True, description="SSL VERSION TO CONNECT")
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




