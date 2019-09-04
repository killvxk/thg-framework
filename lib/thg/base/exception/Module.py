class ModuleNotUseException(Exception):
    def __str__(self):
        return "Please use a module"

class THGBaseException(Exception):
    def __str__(self):
        return "pass"


class THGUserQuitException(THGBaseException):
    def __str__(self):
        return "pass"

class THGShellQuitException(THGBaseException):
    def __str__(self):
        return "pass"


class THGDataException(THGBaseException):
    def __str__(self):
        return "pass"


class THGGenericException(THGBaseException):
    def __str__(self):
        return "pass"


class THGSystemException(THGBaseException):
    def __str__(self):
        return "pass"


class THGFilePathException(THGBaseException):
    def __str__(self):
        return "pass"


class THGConnectionException(THGBaseException):
    def __str__(self):
        return "pass"


class THGThreadException(THGBaseException):
    def __str__(self):
        return "pass"


class THGValueException(THGBaseException):
    def __str__(self):
        return "pass"


class THGMissingPrivileges(THGBaseException):
    def __str__(self):
        return "pass"


class THGSyntaxException(THGBaseException):
    def __str__(self):
        return "pass"


class THGValidationException(THGBaseException):
    def __str__(self):
        return "pass"


class THGMissingMandatoryOptionException(THGBaseException):
    def __str__(self):
        return "pass"


class THGPluginBaseException(THGBaseException):
    def __str__(self):
        return "pass"


class THGPluginDorkException(THGPluginBaseException):
    def __str__(self):
        return "pass"
