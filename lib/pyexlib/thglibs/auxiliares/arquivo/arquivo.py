from thglibs.auxiliares.debug.debug import Debug
import itertools
from base64 import b64encode
from base64 import b32encode
from base64 import b16encode
from io import open
from thg.ThgClass import THG_class


class Arquivos(metaclass=THG_class):
    """
    class resposnsavel por manipular aquivos, com suporte utf-8 no python atual, podendo mudar
    atraver do
    :argument encode="" seu encode
    """

    def __init__(self, arquivo, escrever, tabulacao, encode):
        self.arquivo = arquivo
        self.escrever = escrever
        self.tabulacao = tabulacao
        self.encode = encode

    def ler(arquivo, encode="utf8"):
        """
        :arg arquivo
        :info ler arquivo
        """
        with open(arquivo, "r", encoding=encode) as ll:
            print(ll.read())

    def escrever(arquivo, escrever):
        """
        :info escrever no arquivo
        :param arquivo,escrever:
            :parameter arquivo  => nome+caminho do arquivo
            :parameter escrever => escrever
        :return: arquivo + texto
        """
        try:
            try:
                with open(arquivo, "w") as ll:
                    ll.write(escrever)
                    Debug.CRITICAL("arquivo: " + arquivo)

                    Debug.CRITICAL("escreveu: " + escrever)
            except TypeError:
                print(TypeError)
        except THG_OSError:
            print("erro " + str(OSError))

    def escrever_encode64(arquivo, escrever):
        """
        :info escrever no arquivo com base64
        :param arquivo,escrever:
            :parameter arquivo  => nome+caminho do arquivo
            :parameter escrever => escrever
        :return: arquivo + texto
        """
        with open(arquivo, "w") as ll:
            encode = b64encode(bytes(escrever, 'utf-8'))
            decode = str(encode)[2:-1]
            ll.write(decode)
            Debug.INFO("Arquivo: " + arquivo)

            Debug.CRITICAL("escrita " + decode)

    def escrever_encode32(arquivo, escrever):
        """
        :info escrever no arquivo com base32
        :param arquivo,escrever:
            :parameter arquivo  => nome+caminho do arquivo
            :parameter escrever => escrever
        :return: arquivo + texto
        """
        with open(arquivo, "w") as ll:
            encode = b32encode(bytes(escrever, 'utf-8'))
            decode = str(encode)[2:-1]
            ll.write(decode)
            Debug.CRITICAL("Arquivo: " + arquivo)
            Debug.CRITICAL("escrita " + decode)

    def escrever_encode16(arquivo, escrever):
        """
        :info escrever no arquivo com base16
        :param arquivo,escrever:
            :parameter arquivo  => nome+caminho do arquivo
            :parameter escrever => escrever
        :return: arquivo + texto
        """
        with open(arquivo, "w") as ll:
            encode = b16encode(bytes(escrever, 'utf-8'))
            decode = str(encode)[2:-1]
            ll.write(decode)
            Debug.CRITICAL("arquivo: " + arquivo)
            Debug.CRITICAL("escrita " + decode)

    def Gera(minimo, maximo, char, nome, verbose=""):
        # validacao
        if minimo == 0:
            print("[erro]=[numero maior que zero ou nada]")
            pass
        if maximo == 0:
            print("[erro]=[numero maior que zero ou nada]")
            pass
        elif type(maximo) == "str":
            print("[erro]=[]")
            pass
        elif type(char) == "init":
            print("[erro]=[]")
            pass
        elif type(nome) == "int":
            print("[erro]=[]")
            pass
        elif type(minimo) == "str":
            print("[erro]=[]")
            pass
        word_list_name = nome
        min = minimo
        max = maximo
        chrs = char
        with open(word_list_name, "w") as fl:

            min_length, max_length = int(min), int(max)

            for n in range(min_length, max_length + 1):

                for xs in itertools.product(chrs, repeat=n):

                    dsa = fl.write(''.join(xs) + "\n")

                    if verbose == True:

                        Debug.INFO(''.join(xs))

                    else:

                        pass

    def str_up_especial(min, max, word_list_name, verbose=True):
        chrs = 'abcdefghijklmnopqrstuvwxyz~@#$%^&*()_+=-][}{\|""/?.><,,'.upper()
        with open(word_list_name, "w") as fl:
            min_length, max_length = int(min), int(max)
            for n in range(min_length, max_length + 1):
                for xs in itertools.product(chrs, repeat=n):
                    if verbose == True:
                        dsa = fl.write(''.join(xs) + "\n")
                        Debug.INFO(''.join(xs))
                    else:
                        pass
