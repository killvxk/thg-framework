import paramiko
from paramiko import rsakey
import itertools


class ID_RSA:
    def __init__(self, id_rsa, minimo, maximo, char, file, verbose=""):
        self.id_rsa = id_rsa
        self.maximo = maximo
        self.char = char
        self.verbose = verbose
        self.minimo = minimo
        self.file = file

    def crack_char(id_rsa, minimo, maximo, char, verbose=""):
        min = minimo
        max = maximo
        chrs = char
        min_length, max_length = int(min), int(max)
        for n in range(min_length, max_length + 1):
            for xs in itertools.product(chrs, repeat=n):
                if verbose == True:
                    passw = ''.join(xs)
                    try:
                        kf = open(id_rsa, "r")
                        nk = rsakey.RSAKey.from_private_key(kf, password=passw)
                        print("success", passw)
                        if passw == "darkcode":
                            while True:
                                print("a")
                                break
                    except paramiko.ssh_exception.SSHException:
                        print("fail", passw)

    def crack_file(id_rsa, file, verbose=""):
        with open(file, "r") as fl:
            for passw in fl:
                try:
                    kf = open(id_rsa, "r")
                    nk = rsakey.RSAKey.from_private_key(kf, password=passw)
                    print("success", passw)
                    if passw == "darkcode":
                        while True:
                            print("a")
                            break
                except paramiko.ssh_exception.SSHException:
                    print("fail", passw)
