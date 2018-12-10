import os,socket,sys,platform
from thgconsole.core.CoreUtils.printer import print_info
class thg_add_init:
    def __init__(self):
        pass


    def ipi():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        a = s.getsockname()[0]
        return a


    # def ipe():
    # a = ipgetter.myip()
    # Debug.INFO("[+]ip_interno "+a)
    def is_connected():
        try:
            socket.create_connection(("www.google.com", 80))
            return ("THG_Online")
        except OSError:
            return ("THG_off")


    def check_python_version():
        a = sys.version[0]
        b = sys.version[1]
        c = sys.version[2]
        return a + b + c



    def check_gcc_version():
        gcc1 = platform.python_compiler()[4]
        gcc2 = platform.python_compiler()[5]
        gcc3 = platform.python_compiler()[6]
        gcc4 = platform.python_compiler()[7]
        gcc5 = platform.python_compiler()[8]
        return str(gcc1 + gcc2 + gcc3 + gcc4 + gcc5)

