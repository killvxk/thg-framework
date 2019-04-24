from thglibs.auxiliares.cores.cores import Cores


class Debug:
    """ex:debug
            brainiac_utils.debug.INFO() # obtem informacoes sobre o processo
            brainiac_utils.debug.CRITICAL() #informacoes criticas
            brainiac_utils.debug.ERRO() # informacoes de erro
            brainiac_utils.debug.DEBUG() #debug da funcao
            brainiac_utils.debug.AVISO() #alertas
    """

    def __init__(self, DEBUG, INFO, AVISO, ERRO, CRITICAL):
        self.DEBUG = DEBUG
        self.INFO = INFO
        self.AVISO = AVISO
        self.ERRO = ERRO
        self.CRITICAL = CRITICAL

    def ERRO(self):
        Cores.cores("vermelho", "Erro: " + self)

    def INFO(self):
        Cores.cores("amarelo", "INFO: " + self)

    def CRITICAL(self):
        Cores.cores("vermelho", "CRITICAL: " + self)

    def AVISO(self):
        Cores.cores("amarelo", "AVISO: " + self)

    def DEBUG(self):
        Cores.cores("azul", "DEBUG: " + self)
