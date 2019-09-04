# Guia de desenvolvimento de Plugins

Visão Geral
-----

Para escrever um plugin e utilizá-lo no THG primeiro é necessário:

 * O plugin precisa ser ``class`` e o nome da classe deve ser ``Plugin``
 * A classe ``Plugin`` deve herdar ``lib.thg.thgcmd.cmd2``
 * Deve conter um método chamado ``__init__`` que deve chamar o método ``__init__`` da classe pai ``super().__init__(*args, **kwargs)``
 * Deve conter um método chamado ``onLoad(self, args_raw)`` com os parâmetros ``self`` e ``args_raw``

Como carregar o plugin:
---

 * Basta utilizar o comando ``plugin <nome do plugin>``
