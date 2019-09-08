# Guia de desenvolvimento de módulos 




Fazer o melhor trabalho requer esforços conjuntos de todos.

Todos são bem-vindos para desenvolver módulos, trocar tecnologia de segurança e melhorar as habilidades de desenvolvimento 

Vou insistir em manter a biblioteca de módulos por um longo tempo e gostarioa de ajuda de todos 

visão geral
-------------

Para escrever um módulo completo do thg, você precisa atender aos seguintes requisitos:

 * O módulo deve ser uma `` class`` e o nome da classe é ``Modules``
 * A classe `` Modules`` deve herdar de `` BaseExploit/BaseAuxiliary/BasePost/BasePayload/BaseNops/BaseEvasion`` (introduzido por `` lib.BaseMode.mods import Base*``)
 * O módulo deve conter o método `` __init__``, que deve chamar o método `` __init__`` da classe pai (via `` super ("Modules"", self) .__ init __ () ``)
 * O módulo deve preencher as informações relevantes, usando o método `` self.thg_update_info () ``
 * Os objetivos do POC estão atualmente divididos em tipos `` http`` e `` tcp``, usando `` self.register_tcp_target () `` para registrar alvos do tipo tcp. Registre o tipo de destino http com `` self.register_http_target () ``.
 * Após o registro, o alvo pode ser recuperado usando `` self.options.get_option``.
 * O método `` check`` é usado para detectar vulnerabilidades e não há comportamento de ataque.
 * O método `` exploit`` é usado para implementar o comportamento de ataque, mas não pode ser usado para afetar a operação normal do servidor.
 * Nos métodos `` check`` e `` exploit``, se o teste for bem sucedido, chame o método `` self.results.success () `` para salvar o resultado. Se falha  chamer `` self.results.failure () `` para salvar o resultado.
 * No processo de escrever os módulo do thg, se você usar `` pycharm``, você pode seguir o método acima para ver o código e melhorar sua compreencao. Se você tiver dúvidas ou sugestões, não hesite em entrar em contato comigo.
###
##darkcode357/luiz gustavo correa
###

Case: test unauthorized detection module
----------------------------

Basic code: ::

    import socket
    from lib.BaseMode.mods.Auxiliary.Auxiliary import BaseAuxiliary
    
    class Modules(BaseAuxiliary):
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
            self.register_tcp_target(port_value=6379)

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
Writing module
---------


Aqui está um exemplo de uma vulnerabilidade de acesso não autorizado.
Primeiro crie o arquivo: ``/modules/__tipo_do_modulo__/__nome__/__nome_modulo__.py``
Introduzir a classe `` Base{BaseExploit/BaseAuxiliary/BasePost/BasePayload/BaseNops/BaseEvasion}`` e dentro da class ```base{que voce escolheu}``` tem a class `` BaseOption``  e o nome da class tem que do modulo tem que ser `` Modules``, herdando a classe `` Base{mod}``
Todos os módulos devem herdar a classe `` Base{mode}`` e o nome da classe deve ser `` Modules`` e a class`` BaseOption``e automaticamente  importada  para registrar os parâmetros do módulo.

Declarar a classe Modules
--------------

Primeira classe de escrita ::

    from lib.BaseMode.mods.Auxiliary.Auxiliary import BaseAuxiliary
    from lib.BaseMode.mods.Evasion.Evasion import BaseEvasion
    from lib.BaseMode.mods.Exploit.Exploit import BaseExploit
    from lib.BaseMode.mods.Nops.Nops import BaseNops
    from lib.BaseMode.mods.Payload.Payload import BasePayload
    from lib.BaseMode.mods.Post.Post import BasePost
    from lib.BaseMode.mods.Osint.Osint import BaseOsint
    
    class Modules(BaseAuxiliary):
        pass

Complete the __init__ method
-----------------

Então complete o método `` __init__``: ::

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
        Self.register_tcp_target(port_value=6379)

Para explicar isso, primeiro observe a primeira linha do método `` __init__``: ::

    Super (Modules, self) .__ init __ ()

Esta linha é necessária, e você precisa chamar o método `` __init__`` da classe pai para inicializar o módulo.

Em seguida, atualize as informações do módulo usando o método `` self.thg_update_info``: ::
    
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

Então use o método `` self.register_tcp_target`` para registrar um alvo do tipo tcp. Este método registra automaticamente os seguintes parâmetros para nós:
       
    self.register_options([
      BaseOption(name="HOST", required=True, description="The IP address to be tested"),
      BaseOption(name="PORT", required=True, description="The port to be tested", value=port_value),
      BaseOption(name="TIMEOUT", required=True, description="Connection timeout", value=timeout_value),
      BaseOption(name="THREADS", required=True, description="The number of threads", value=threads_value)
        ])

Para nossas vulnerabilidades não autorizadas de ****, HOST e PORT são suficientes, portanto não há necessidade de registrar os parâmetros adicionais.
Se você precisar registrar parâmetros adicionais, você pode chamar o método `` self.register_options``, passando uma lista contendo o objeto `` BaseOption``.

Método de importação automatico da class base que voce escolheu 

Complete o método de verificação
--------------

O método de verificação grava principalmente para detectar a existência de uma vulnerabilidade e não há comportamento de ataque. código mostra como abaixo:
        
     Def check(self):
        Host = self.options.get_option("HOST")
        Port = int(self.options.get_option("PORT"))
        Timeout = int(self.options.get_option("TIMEOUT"))

        Try:
            Socket.setdefaulttimeout(timeout)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            S.connect((host, port))
            S.send(bytes("INFO\r\n", encoding="utf-8"))
            Result = s.recv(1024)
            If bytes("mod_version", encoding="utf-8") in result:
                Self.results.success(
                    Data={
                        "host": host,
                        "port": port,
                    },
                    Message="Host {host}:{port} exists mod unauthorized vulnerability".format(host=host, port=port)
                )
            Else:
                Self.results.failure(
                    Error_message="Host {host}:{port} does not exists mod unauthorized vulnerability".format(
                        Host=host,
                        Port=port
                    )
                )
        Except Exception as e:
            Self.results.failure(error_message="Host {host}:{port}: {error}".format(host=host, port=port, error=e))
        Return self.results

Primeiro, as primeiras três linhas usam o método `` self.options.get_option () `` para obter os parâmetros do módulo.

Então o processo exp é executado.

Execução bem-sucedida, encontrou uma vulnerabilidade, chamada de método `` self.results.success``,  dados de entrada e informações de sucesso: ::

    Self.results.success(
        Data={
            "host": host,
            "port": port,
        },
        Message="Host {host}:{port} exists mod unauthorized vulnerability".format(host=host, port=port)
    )

Se a vulnerabilidade não existe, o método `` self.results.failure`` é executado, e a mensagem de falha é passada em: ::

    Self.results.failure(
        Error_message="Host {host}:{port} does not exists mod unauthorized vulnerability".format(
            Host=host,
            Port=port
        )
    )

O método de verificação deve retornar `` self.results`` ::

    Return self.results

Complete o método de exploração
----------------

Essa vulnerabilidade é relativamente simples, portanto, você não pode retornar o método self.check sem implementar o método de exploração. ::
     
     Def exploit(self):
         Return self.check()

O método exploit também deve retornar `` self.results``, porque o método de verificação também retorna `` self.results``, então você pode chamar `` self.check () `` diretamente.

Mais casos
--------------

Agora que a maior parte da funcionalidade da estrutura foi concluída, vou começar a escrever alguns módulos.

Você pode consultar os módulos escritos  para completar seus próprios módulos.

Todos os módulos estão no diretório modules do repositório do github.