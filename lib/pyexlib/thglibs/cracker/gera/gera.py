import errno
import itertools
import os


class Gera_wordlist():
    """
    gerador de wordlist totalmente customizado
    ex:
        Gera_wordlist.Gera(i,i,str,str,verbose=True/False)
        i = inteiro
        str = string
        verbose = True/false
        [info]
        x1=[x]=[minimo de caracteres]
        x2=[x]=[maximo de caracteres]
        str1[str]=[caracteres[abcde...etc]]
        str2[str]=[nome da wordlist]
        verbose=True[se vc habilitar o verbose vc podera ver a saida da sua wordlist]

    thg_exemplo:
        Gera_wordlist.Gera(1,2,"abc123","test",verbose=True)
    saida:
    a
    b
    c
    1
    2
    3
    aa
    ab
    ac
    a1
    a2
    a3
    ba
    bb
    bc
    b1
    b2
    b3
    ca
    cb
    cc
    c1
    c2
    c3
    1a
    1b
    1c
    11
    12
    13
    2a
    2b
    2c
    21
    22
    23
    3a
    3b
    3c
    31
    32
    33

    """

    def __init__(self, maximo, minimo, char, nome):
        self.maximo = maximo
        self.minimo = minimo
        self.char = char
        self.nome = nome

    def Gera(minimo, maximo, char, nome, verbose=""):
        # validacao
        if minimo == 0:
            print("[erro]=[numero maior que zero ou nada]")
            pass
            exit()
        if maximo == 0:
            print("[erro]=[numero maior que zero ou nada]")
            pass
            exit()
        elif type(maximo) == "str":
            print("[erro]=[]")
            pass
            exit()
        elif type(char) == "init":
            print("[erro]=[]")
            pass
            exit()
        elif type(nome) == "int":
            print("[erro]=[]")
            exit()
            pass
        elif type(minimo) == "str":
            print("[erro]=[]")
            exit()

        word_list_name = nome
        min = minimo
        max = maximo
        chrs = char
        min_length, max_length = int(min), int(max)
        for n in range(min_length, max_length + 1):
            for xs in itertools.product(chrs, repeat=n):
                if verbose == True:
                    print(''.join(xs))
                else:
                    pass
