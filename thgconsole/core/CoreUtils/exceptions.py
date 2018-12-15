class THGtException(Exception):
    #execao da aplicacao
    #aplication execption
    def __init__(self, msg: str = "[*]erro"):
        super(THGtException, self).__init__(msg)


class OptionValidationError(THGtException):
    pass#execpt erro in option modules
        #execao de erro no modulos da aplicacao


class StopThreadPoolExecutor(THGtException):
    pass#except thread on module
        #execao das threads nos modulos
