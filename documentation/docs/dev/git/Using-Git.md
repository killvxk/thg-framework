Use esta coleção de recursos para trabalhar com o repositório git do thg Framework.

* [Cheatsheet | Git cheatsheet](dafko)
* [Sites de referência | Sites de referência do Git]
* [Configurando um ambiente de desenvolvimento] - isso orientará você na criação de uma solicitação pull
* [Landing Pull Requests] - este é o procedimento pelo qual os principais desenvolvedores do Metasploit passam para mesclar sua solicitação
* [Remoção de ramificação remota]

Uma bifurcação é quando você captura instantaneamente a base de código de outra pessoa no seu próprio repositório, 
presumivelmente no gitlab.com, e essa base de código pode ter suas próprias ramificações, 
mas você geralmente captura instantaneamente a ramificação principal. Você geralmente clona seu fork na sua máquina local. 
Você cria seus próprios ramos, que são ramificações de seu próprio fork. Esses snapshots, mesmo que enviados ao seu github, 
não fazem parte da base de código original, neste caso, o darkcode357/thg-framework. Se você enviar uma solicitação de recebimento, 
sua ramificação (geralmente) poderá ser transferida para a ramificação principal da base de código original (geralmente ... você poderá ser transferido para uma ramificação experimental ou algo assim, se o seu código for uma alteração maciça ou algo assim, mas isso não é típica).

Você apenas bifurca uma vez, clona quantas vezes voce quiser e nas codificar e ramifica, confirma e empurra quantas vezes quiser (nem sempre precisa empurrar, pode empurrar mais tarde ou não , mas você precisará enviar antes de fazer uma solicitação de recebimento, também conhecida como PR), e enviará um PR quando estiver pronto. Ver abaixo
```
gitlab.com/darkcode357/thg-framework/ --> fork --> github.com/<...>/thg-framework
    ^                                                          |
    |                               git clone git://gitlab.com/<...>/thg-framework.git
    |                                                          |
    `-- accepted <-- pull request                              V
                      ^                        /home/<...>/repo/thg-framework
                      |                                |              |          |
   github.com/<...>/thg-framework/branch_xyz    |              |          |
                      |                                |              V          V
                      |                                V           branch_abc   ...
                      `--       push       <--      branch_xyz
```

