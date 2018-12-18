from .toplevel import *

'''
# coding=utf-8
from __future__ import absolute_import
import platform
import os
import subprocess
from thglibs.auxiliares.debug.debug import Debug
from thglibs.auxiliares.cores.cores import Cores
from thglibs.auxiliares.thg_check_hosts.check_host import Check_all
from thglibs.version.version import version
import socket
#import ipgetter
import sys
from .toplevel import *

class check_brainiac:
    def __init__(self):
        pass

    def ipi():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        a = s.getsockname()[0]
        Debug.INFO("[+]ip_interno " + a)
    #def ipe():
        #a = ipgetter.myip()
        #Debug.INFO("[+]ip_interno "+a)
    def is_connected():
        try:
            socket.create_connection(("www.google.com", 80))
            Debug.INFO("[+]THG_Online")
        except OSError:
            Debug.INFO("[+]THG_off")
    def check_vm():
        pass
    def check_python_version():
        a = sys.version[0]
        b = sys.version[1]
        c = sys.version[2]
        t = a+b+c
        if t == "3.6":
            Debug.INFO("[+]python 3.6")
        else:
            exit(1)
    def check_gcc_version():
        gcc1 = platform.python_compiler()[4]
        gcc2 = platform.python_compiler()[5]
        gcc3 = platform.python_compiler()[6]
        gcc4 = platform.python_compiler()[7]
        gcc5 = platform.python_compiler()[8]
        version = str(gcc1 + gcc2 + gcc3 + gcc4 + gcc5)
        Debug.INFO("[+]gcc "+version)
    def check_id():
        if os.getuid() != 0:
            Debug.CRITICAL("[+]rode como root")
            Debug.CRITICAL("sudo python")
            Debug.CRITICAL("import thg")
            exit(1)
    def check_programas():
        list_cmd = ['iptables']
        for cmd in list_cmd:
            exist = subprocess.call('command -v ' + cmd + '>> /dev/null', shell=True)
            if exist == 0:
                pass
            else:
                print("efetue a instalacao do [%s]"%cmd)
                exit(1)
        Debug.INFO("[+]check programas =>[ok]")


if not platform.architecture()[0].startswith('64'):
    """Determina se o interpretador atual do Python é suportado pelo Brainiac"""
    Debug.CRITICAL("[+]Brainiac não suporta  o usod do Python 32 bits. Use uma versão de 64 bits.")
    exit(1)

else:

    os.system("clear")
    version()
    check_brainiac.check_id()

    Cores.cores("vermelho","[+]thg importado")

    checkvm = input("ctf_local ou ctf_online ? [ctf_local/ctf_online] =>")
    if checkvm == "ctf_local":
        host = input("host/ranger=>")
        port = input("ports(1-10)/port>")
        protocolo = input("protocolo (tcp/udp)=>")
        Check_all.Check_All(host,port,protocolo)
    elif checkvm =="ctf_online":
        pass
    else:

        pass

    Cores.cores("amarelo","[+]use help() para ter mais informacoes")
    Cores.cores("vermelho","###############################")
    Cores.cores("azul","[+]iniaciando checking")
    check_brainiac.is_connected()
    #check_brainiac.ipe()
    check_brainiac.ipi()
    check_brainiac.check_python_version()
    check_brainiac.check_gcc_version()
    check_brainiac.check_programas()
'''
