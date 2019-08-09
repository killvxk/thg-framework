import socket
from lib.thg.core.mods.Auxiliary.Auxiliary import BaseAuxiliary_Crawler

class Modules(BaseAuxiliary_Crawler):
    def __init__(self):
        super(Modules, self).__init__()
        self.thg_update_info({
            "name": "base",
            "description": "descricao da modulo",
            "author": ["darkcode"],
            "references": [
                "referencia ",
            ],
            "disclosure_date": "data do modulo",
            "service_name": "nome do servico",
            "service_version": "versao do servico",
        })
        # Como o modulo so preciasa do thg, entao。
        self.register_crawler()

    def check(self):
        #Esses três parâmetros são registrados pelo método de destino self.register tcp, que pode ser chamado diretamente aqui.
        host = self.options.get_option("HOST")
        port = int(self.options.get_option("PORT"))
        timeout = int(self.options.get_option("TIMEOUT"))

        #Todo o processo de execução do teste é melhor colocado na tentativa(try) e, em seguida, capturar o erro no except diretamente chamando self.results.failure para imprimir o erro.
        try:
            socket.setdefaulttimeout(timeout)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.send(bytes("INFO\r\n", encoding="utf-8"))
            result = s.recv(1024)
            if bytes("INFO", encoding="utf-8") in result:
                #Existe uma lacuna, a chamada dos dados deste método pode ser passada para um dicionário, sendo atualmente inútil ou não.
                self.results.success(
                    data={
                        "host": host,
                        "port": port,
                    },
                    #Como vários alvos podem ser executados, é melhor escrever o destino e a porta no resultado para facilitar a identificação.
                    message="Host {host}:{port} exists *** unauthorized vulnerability".format(host=host, port=port)
                )
            else:
                # Não existe vulnerabilidade. Chame o método self.results.failure para passar a mensagem de erro
                self.results.failure(
                    error_message="Host {host}:{port} does not exists *** unauthorized vulnerability".format(
                        host=host,
                        port=port
                    )
                )
        except Exception as e:
            # Erro de execução, use self.results.failure para passar a mensagem de erro.
            self.results.failure(error_message="Host {host}:{port}: {error}".format(host=host, port=port, error=e))
        return self.results

    def exploit(self):
        return self.check()