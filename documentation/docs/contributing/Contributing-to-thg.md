===================== Guia de desenvolvimento de módulos =====================

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

Case: redis unauthorized detection module
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

Here is an example of a redis unauthorized vulnerability.

First create the file: ``/modules/exploits/server/redis_unauthorized.py``

Introduce the ``BaseExploit`` class and the ``ExploitOption`` class, and write the ``Exploit`` class, inheriting the ``BaseExploit`` class

All modules must inherit the ``BaseExploit`` class and the class name must be ``Exploit`` and ``ExploitOption`` to register the module parameters.

Declare the Exploit class
--------------

First write class ::

    From lib.BaseExploit import BaseExploit
    From lib.ExploitOption import ExploitOption


    Class Exploit(BaseExploit):
        Pass

Complete the __init__ method
-----------------

Then complete the ``__init__`` method: ::

    Def __init__(self):
        Super(Exploit, self).__init__()
        Self.thg_update_info({
            "name": "redis unauthorized",
            "description": "redis unauthorized",
            "author": ["unknown"],
            "references": [
                "https://www.freebuf.com/column/158065.html",
            ],
            "disclosure_date": "2019-02-28",
            "service_name": "redis",
            "service_version": "*",
        })
        Self.register_tcp_target(port_value=6379)

To explain this, first look at the first line of the ``__init__`` method: ::

    Super(Exploit, self).__init__()

This line is required, and you need to call the parent class's ``__init__`` method to initialize the module.

Then update the module information using the ``self.thg_update_info`` method: ::

    Self.thg_update_info({
        "name": "redis unauthorized",
        "description": "redis unauthorized",
        "author": ["unknown"],
        "references": [
            "https://www.freebuf.com/column/158065.html",
        ],
        "disclosure_date": "2019-02-28",
        "service_name": "redis",
        "service_version": "*",
    })

Then use the ``self.register_tcp_target`` method to register a target of type tcp. This method automatically registers the following parameters for us: ::

    Self.register_options([
        ExploitOption(name="HOST", required=True, description="The IP address to be tested"),
        ExploitOption(name="PORT", required=True, description="The port to be tested", value=port_value),
        ExploitOption(name="TIMEOUT", required=True, description="Connection timeout", value=timeout_value),
        ExploitOption(name="THREADS", required=True, description="The number of threads", value=threads_value)
    ])

For our redis unauthorized vulnerabilities, HOST and PORT are sufficient, so there is no need to register additional parameters.

If you need to register additional parameters, you can call the ``self.register_options`` method, passing in a list containing the ``ExploitOption`` object.

``ExploitOption`` import method: ``from lib.ExploitOption import ExploitOption``

Complete the check method
--------------

The check method mainly writes to detect the existence of a vulnerability, and there is no attack behavior. code show as below: ::

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
            If bytes("redis_version", encoding="utf-8") in result:
                Self.results.success(
                    Data={
                        "host": host,
                        "port": port,
                    },
                    Message="Host {host}:{port} exists redis unauthorized vulnerability".format(host=host, port=port)
                )
            Else:
                Self.results.failure(
                    Error_message="Host {host}:{port} does not exists redis unauthorized vulnerability".format(
                        Host=host,
                        Port=port
                    )
                )
        Except Exception as e:
            Self.results.failure(error_message="Host {host}:{port}: {error}".format(host=host, port=port, error=e))
        Return self.results

First, the first three lines use the ``self.options.get_option()`` method to get the module parameters.

Then the exp process is executed.

Successful execution, found a vulnerability, called the ``self.results.success`` method, incoming data and success information: ::

    Self.results.success(
        Data={
            "host": host,
            "port": port,
        },
        Message="Host {host}:{port} exists redis unauthorized vulnerability".format(host=host, port=port)
    )

If the vulnerability does not exist, the ``self.results.failure`` method is executed, and the failure message is passed in: ::

    Self.results.failure(
        Error_message="Host {host}:{port} does not exists redis unauthorized vulnerability".format(
            Host=host,
            Port=port
        )
    )

The check method must return ``self.results``. ::

    Return self.results
Complete the exploit method
----------------

This vulnerability is relatively simple, so you can not return the self.check method without implementing the exploit method. ::

     Def exploit(self):
         Return self.check()

The exploit method must also return ``self.results``, because the check method also returns ``self.results``, so you can call ``self.check()`` directly.

More cases
--------------

Now that most of the framework's functionality has been completed, I will start writing some modules myself.

You can refer to the modules I have written to complete their own modules.

All modules are in the modules directory of the github repository.
