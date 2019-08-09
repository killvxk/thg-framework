from lib.thg.base.BaseOptions import BaseOption
from lib.thg.base.BaseOptions import BaseOptions
from lib.thg.base.BaseResult import BaseResult

class BaseAuxiliary_Brute:
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

    def register_tcp_target_brute(self, port_value=None, timeout_value=5, threads_value=1):
      self.target_type = "tcp"
      self.register_options([
        BaseOption(name="HOST", required=True, description="The IP address to be tested"),
        BaseOption(name="PORT", required=True, description="The port to be tested", value=port_value),
        BaseOption(name="TIMEOUT", required=True, description="Connection timeout", value=timeout_value),
        BaseOption(name="THREADS", required=True, description="The number of threads", value=threads_value),
        BaseOption(name='USERNAME', required=True, description='A specific username to authenticate as'),
        BaseOption(name='PASSWORD', required=True, description='A specific password to authenticate with'),
        BaseOption(name='USER_FILE', required=True, description="File containing usernames, one per line"),
        BaseOption(name='PASS_FILE', required=True, description="File containing passwords, one per line"),
        BaseOption(name='USERNAME', required=False, description='A specific username to authenticate as'),
        BaseOption(name='PASSWORD', required=False, description='A specific password to authenticate with'),
        BaseOption(name='USER_FILE', required=False, description="File containing usernames, one per line"),
        BaseOption(name='PASS_FILE', required=False, description="File containing passwords, one per line"),
        BaseOption(name='USERPASS_FILE', required=False, description="File containing users and passwords separated by space, one pair per line"),
        BaseOption(name='BRUTEFORCE_SPEED', required=True, description="How fast to bruteforce, from 0 to 5"),
        BaseOption(name='VERBOSE', required=True, description="Whether to print output for all attempts"),
        BaseOption(name='BLANK_PASSWORDS', required=False, description="Try blank passwords for all users"),
        BaseOption(name='USER_AS_PASS', required=False, description="Try the username as the password for all users"),
        BaseOption(name='DB_ALL_CREDS', required=False,description="Try each user/password couple stored in the current database"),
        BaseOption(name='DB_ALL_USERS', required=False,description="Add all users in the current database to the list"),
        BaseOption(name='DB_ALL_PASS', required=False,description="Add all passwords in the current database to the list"),
        BaseOption(name='STOP_ON_SUCCESS', required=True,description="Stop guessing when a credential works for a host"),
        BaseOption(name='REMOVE_USER_FILE', required=True,description="Automatically delete the USER_FILE on module completion", value=False),
        BaseOption(name='REMOVE_PASS_FILE', required=True,description="Automatically delete the PASS_FILE on module completion", value=False),
        BaseOption(name='REMOVE_USERPASS_FILE', required=True,description="Automatically delete the USERPASS_FILE on module completion", value=False),
        BaseOption(name='PASSWORD_SPRAY', required=True,description="Reverse the credential pairing order. For each password, attempt every possible user.",value=False),
        BaseOption(name='TRANSITION_DELAY', required=False,description="Amount of time (in minutes) to delay before transitioning to the next user in the array (or password when PASSWORD_SPRAY=true)",value=0),
        BaseOption(name='MaxGuessesPerService', required=False,description="Maximum number of credentials to try per service instance. If set to zero or a non-number, this option will not be used.",value=0),
        BaseOption(name='MaxMinutesPerService', required=False,description="Maximum time in minutes to bruteforce the service instance. If set to zero or a non-number, this option will not be used.",value=0),
        BaseOption(name='MaxGuessesPerUser', required=False,description="Maximum guesses for a particular username for the service instance.Note that users are considered unique among different services")
      ])
    def register_http_target_brute(self, timeout_value=5, threads_value=1):
      self.target_type = "http"
      self.register_options([
        BaseOption(name="URL", required=True, description="The url to be tested"),
        BaseOption(name="TIMEOUT", required=True, description="Connection timeout", value=timeout_value),
        BaseOption(name="THREADS", required=True, description="The number of threads", value=threads_value),
        BaseOption(name='USERNAME', required=True, description='A specific username to authenticate as'),
        BaseOption(name='PASSWORD', required=True, description='A specific password to authenticate with'),
        BaseOption(name='USER_FILE', required=True, description="File containing usernames, one per line"),
        BaseOption(name='PASS_FILE', required=True, description="File containing passwords, one per line"),
        BaseOption(name='USERNAME', required=False, description='A specific username to authenticate as'),
        BaseOption(name='PASSWORD', required=False, description='A specific password to authenticate with'),
        BaseOption(name='USER_FILE', required=False, description="File containing usernames, one per line"),
        BaseOption(name='PASS_FILE', required=False, description="File containing passwords, one per line"),
        BaseOption(name='USERPASS_FILE', required=False,
                   description="File containing users and passwords separated by space, one pair per line"),
        BaseOption(name='BRUTEFORCE_SPEED', required=True, description="How fast to bruteforce, from 0 to 5"),
        BaseOption(name='VERBOSE', required=True, description="Whether to print output for all attempts"),
        BaseOption(name='BLANK_PASSWORDS', required=False, description="Try blank passwords for all users"),
        BaseOption(name='USER_AS_PASS', required=False, description="Try the username as the password for all users"),
        BaseOption(name='DB_ALL_CREDS', required=False,
                   description="Try each user/password couple stored in the current database"),
        BaseOption(name='DB_ALL_USERS', required=False,
                   description="Add all users in the current database to the list"),
        BaseOption(name='DB_ALL_PASS', required=False,
                   description="Add all passwords in the current database to the list"),
        BaseOption(name='STOP_ON_SUCCESS', required=True,
                   description="Stop guessing when a credential works for a host"),
        BaseOption(name='REMOVE_USER_FILE', required=True,
                   description="Automatically delete the USER_FILE on module completion", value=False),
        BaseOption(name='REMOVE_PASS_FILE', required=True,
                   description="Automatically delete the PASS_FILE on module completion", value=False),
        BaseOption(name='REMOVE_USERPASS_FILE', required=True,
                   description="Automatically delete the USERPASS_FILE on module completion", value=False),
        BaseOption(name='PASSWORD_SPRAY', required=True,
                   description="Reverse the credential pairing order. For each password, attempt every possible user.",
                   value=False),
        BaseOption(name='TRANSITION_DELAY', required=False,
                   description="Amount of time (in minutes) to delay before transitioning to the next user in the array (or password when PASSWORD_SPRAY=true)",
                   value=0),
        BaseOption(name='MaxGuessesPerService', required=False,
                   description="Maximum number of credentials to try per service instance. If set to zero or a non-number, this option will not be used.",
                   value=0),  # Tracked in @@guesses_per_service
        BaseOption(name='MaxMinutesPerService', required=False,
                   description="Maximum time in minutes to bruteforce the service instance. If set to zero or a non-number, this option will not be used.",
                   value=0),  # Tracked in @@brute_start_time
        BaseOption(name='MaxGuessesPerUser', required=False,
                   description="Maximum guesses for a particular username for the service instance.Note that users are considered unique among different services, so auser at 10.1.1.1:22 is different from one at 10.2.2.2:22, and both willbe tried up to the MaxGuessesPerUser limit.	If set to zero or a non-number,this option will not be used")

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







'''

'''