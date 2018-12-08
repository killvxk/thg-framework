class THGtException(Exception):
    def __init__(self, msg: str = ""):
        super(THGtException, self).__init__(msg)


class OptionValidationError(THGtException):
    pass


class StopThreadPoolExecutor(THGtException):
    pass
