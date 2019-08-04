import os,socket,sys,platform
from getmac.getmac import get_mac_address

class thg_add_init:
    #show mor info in banner thg
    #mostra mais informacoes no banner do thg
    def __init__(self):
        pass


    def ipi():
        #return internal ip
        #retorna o ip interno
        try:
            import socket
            return [l for l in (
            [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [
                [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
                 [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
        except Exception:
            return "off"


    # def ipe():
    # a = ipgetter.myip()
    # Debug.INFO("[+]ip_interno "+a)
    def is_connected():
        #check connect
        ##verifica a conexao
        try:
            import pycurl
            c = pycurl.Curl()
            c.setopt(pycurl.OPT_CERTINFO, 1)
            c.setopt(pycurl.URL, "https://python.org")
            c.setopt(pycurl.FOLLOWLOCATION, 1)
            return c.getinfo(pycurl.HTTP_CODE)
        except OSError:
            return ("THG_off")


    def check_python_version():
        #check python version
        #verifica a versao do python
        a = sys.version[0]
        b = sys.version[1]
        c = sys.version[2]
        return a + b + c



    def check_gcc_version():
        #check gcc version
        #verifica a versao do gcc
        gcc1 = platform.python_compiler()[4]
        gcc2 = platform.python_compiler()[5]
        gcc3 = platform.python_compiler()[6]
        gcc4 = platform.python_compiler()[7]
        gcc5 = platform.python_compiler()[8]
        return str(gcc1 + gcc2 + gcc3 + gcc4 + gcc5)
    def get_mac():
        #return mac
        #retorna o mac
        return get_mac_address()
