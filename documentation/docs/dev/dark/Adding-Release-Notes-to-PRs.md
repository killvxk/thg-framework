* As notas de versão informam nossos usuários sobre o material que estamos enviando em cada versão. Observando nossas notas de versão, nossos usuários devem ser capazes de entender facilmente o que há de novo, o que foi corrigido e o que foi alterado no lançamento. Portanto, todos os PRs, exceto pequenas correções e ajustes, devem ter notas de versão. 
* Para adicionar uma nota de versão a uma solicitação pull, você precisará adicioná-la como um comentário, assim:

Você precisará marcar o comentário para inclusão nas notas de versão usando o cabeçalho `# Release Notes '. Depois de aplicar o cabeçalho das notas de versão, você pode inserir o texto das notas de versão que deseja usar.
É isso aí! Depois de adicionar o texto das notas de versão, poderemos extraí-las das solicitações pull quando executamos nosso script de notas de versão e compilamos em um único documento.

### Como escrever notas de versão

Ok, agora que você sabe como adicionar uma nota de versão, está se perguntando o que deveria escrever.
Basicamente, uma nota de versão resume a solicitação de recebimento e descreve o valor do reparo / recurso para o usuário. Cada nota de versão possui um título, um número PR e uma breve descrição.
Aqui está um exemplo de como uma nota de versão se parece:

>a class plugin esta funcionando 

#### Notas da versão para aprimoramentos

Um aprimoramento indica que um aprimoramento ou novo recurso foi adicionado à estrutura. Os aprimoramentos incluem itens como módulos auxiliares, módulos pós-exploração e novos payloads.

Ao escrever notas de versão para um aprimoramento, tente responder às seguintes perguntas:

* Qual é o aprimoramento?
* Por que é valioso ou importante para os usuários?
* Como eles podem usá-lo?

Por exemplo, a seguir, uma nota de versão para um aprimoramento:

> Os novos comandos 'plugin $plugin_name, plugins' permite executar pesquisas de plugins
>
#### Notas da versão para defeitos
Um defeito é uma correção para um problema que fazia com que um recurso ou funcionalidade específico não funcionasse da maneira esperada. Basicamente, um defeito indica que algo foi quebrado e foi corrigido.

Ao escrever notas de versão para um defeito, tente responder às seguintes perguntas:

* O que foi quebrado?
* Como foi consertado?
* Por que isso é importante para os usuários?

Aqui está um exemplo de um defeito:

> O cabeçalho do email continha cabeçalhos de data e assunto duplicados, o que fazia com que servidores de email como o AWS SES rejeitassem os emails. Essa correção remove os cabeçalhos duplicados para que as campanhas possam enviar e-mails com êxito.

#### Notas da versão para explorações

Uma exploração é um módulo que tira proveito de uma vulnerabilidade e fornece algum tipo de acesso ao destino. Nós chamamos explorações explicitamente porque elas são gostosas.

Ao escrever notas de versão para uma exploração, tente responder às seguintes perguntas:

* Qual vulnerabilidade o módulo está explorando?
* Que tipo de acesso você pode obter com o módulo?
* Você precisa de credenciais para explorar a vulnerabilidade?

E, finalmente, aqui está um exemplo de exploits:

> Este módulo permite explorar o HP Data Protector, um sistema de backup e recuperação, para carregar remotamente arquivos no compartilhamento de arquivos. As versões 6.10, 6.10 e 6.20 são vulneráveis. Você não precisa se autenticar para explorar esta vulnerabilidade.
