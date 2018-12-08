import nmap
from datetime import datetime
from thglibs.auxiliares.debug.debug import Debug


class Check_all:
    def __init__(self, host, ports, protocolo, timeout, ranger):
        self.host = host
        self.ports = ports
        self.protocolo = protocolo
        self.timeout = timeout
        self.ranger = ranger

    def Check_All(ranger, ports, protocolo):
        t1 = datetime.now()
        nmScan = nmap.PortScanner()
        nmScan.scan(ranger, ports)
        for port in nmScan[ranger][protocolo]:
            thisDict = nmScan[ranger][protocolo][port]
            if thisDict["state"] == "open":
                pport = [80, 8080, 443, 31337]
                prod = thisDict['product']
                if port in pport:
                    Debug.CRITICAL("iniciando scanner ofensivo na [porta =>[%s] => %s]" % (port, prod))
                else:
                    Debug.CRITICAL("pass sem autoinit [requer metodos manuais ] [porta =>[%s] => %s]" % (port, prod))
