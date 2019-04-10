# Olá Mundo!

Obrigado pelo seu interesse em fazer Metasploit - e, portanto, o
mundo - um lugar melhor! Antes de começar, revise nossa
[Código de conduta]. Existem várias maneiras de ajudar além de apenas escrever código:
 - [Envie bugs e solicitações de recursos] com informações detalhadas sobre o seu problema ou ideia.
 - [Ajude os usuários com problemas em aberto] ou [ajude os colegas a testar as solicitações de recebimento recentes].
 - [Relate uma vulnerabilidade de segurança no próprio thg] para o darkcode0x00.
 - Envie um módulo atualizado ou novo! Estamos sempre ansiosos pelas seus novas integrações ou recursos. Não sabe por onde começar? Configure um [ambiente de desenvolvimento] e, em seguida, vá até o ExploitDB para procurar por [exploits de prova de conceito] para voces terem uma boa base de como criar um novo modulo.

# Contribuindo para o THG

Aqui está uma pequena lista de fazer e não fazer para garantir que suas valiosas contribuições realmente façam
no branch master do Metasploit. Se você não se importa em seguir estas regras, sua contribuição
**Será fechado. Desculpa!

## Contribuições do Código

*** Continue com o [Guia de estilo do Ruby] e use o [Rubocop] para encontrar problemas comuns de estilo.
*   siga a [regra 50/72] para mensagens de commit do Git.
*    licencie seu código como BSD 3-clause, BSD 2-clause, ou MIT.
*   **Crie** um [tópico] para trabalhar em vez de trabalhar diretamente no `mestre` para preservar
  história do seu pedido de psuh. Veja [PR#8000] para um exemplo de perda de histórico de commit assim que
  você atualiza seu próprio branch master.

### pedidos de extração

* direcione sua solicitação de recebimento para a ** ramificação principal **.
* especifica um título descritivo para facilitar a busca por sua solicitação pull.
* inclui [saída do console], especialmente para efeitos observáveis ​​em `thgconsole`.
* listar [etapas de verificação] para que seu código seja testável.
* [questões associadas a referência] na sua descrição de solicitação pull.
* Não deixe sua descrição de solicitação pull em branco.
* Não abandone seu pedido pull. Ser receptivo nos ajuda a posicionar seu código mais rapidamente.

O pedido de pull [PR#9966] é um bom exemplo a seguir.

#### Novos módulos

*  Defina `thgfixmod` para corrigir quaisquer erros ou avisos que surjam como um [pré-consolidação].
*  use os diversos mixin [API] s do módulo.
*  Não inclui mais de um módulo por solicitação pull.
*  inclui instruções sobre como configurar o ambiente ou software vulnerável.
*  inclui [Documentação do Módulo] mostrando exemplos de execuções.
*  envie novos [scripts]. Scripts são enviados como exemplos para automatizar tarefas locais e qualquer coisa "séria" pode ser feita com post modules e exploits locais.

#### Código da biblioteca

* ** Faça ** testes de [RSpec] - até mesmo a menor alteração em uma biblioteca pode quebrar o código existente.
** Siga ** [Better Specs] - é como o guia de estilo para especificações.
* ** Faça ** escreva a documentação [YARD] - isto torna mais fácil para as pessoas usarem o seu código.
* ** Não ** conserte muitas coisas em um único pedido. Pequenas correções são mais fáceis de validar.

#### Correções de bugs

* ** Do ** inclui etapas de reprodução na forma de etapas de verificação.
* ** Faça ** link para qualquer [Issues] correspondente no formato de 'See # 1234` na sua descrição de commit.

## Relatório de erros

Por favor, relate as vulnerabilidades no software Rapid7 diretamente para security@rapid7.com. Para mais informações sobre nossa política de divulgação e a abordagem da Rapid7 para divulgação coordenada, [head over here] (https://www.rapid7.com/security).

Ao relatar problemas do Metasploit:
* ** Faça ** uma descrição detalhada do seu bug e use um título descritivo.
* ** Do ** inclui etapas de reprodução, rastreamentos de pilha e qualquer coisa que possa nos ajudar a corrigir seu bug.
* ** Não ** arquive relatórios duplicados; pesquise seu bug antes de preencher um novo relatório.

Se você precisar de mais orientação, fale com o corpo principal de contribuidores de código aberto sobre nossos
[Folga de THG]

Por fim, ** obrigado ** por aproveitar alguns momentos para ler até aqui! Você já está bem à frente do
curva, então continue assim!

[Code of Conduct]:https://github.com/darkcode357/thg-framework/wiki/CODE_OF_CONDUCT.md
[Help fellow users with open issues]:https://github.com/darkcode357/thg-framework/issues
[help fellow committers test recently submitted pull requests]:https://github.com/darkcode357/thg-framework/pulls
[development environment]:https://github.com/darkcode357/thg-framework/wiki/Setting-Up-a-THG-Development-Environment
[proof-of-concept exploits]:https://www.exploit-db.com/search?verified=true&hasapp=true&nomsf=true
[Ruby style guide]:https://github.com/Khan/style-guides/blob/master/style/python.md
[50/72 rule]:http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
[topic branch]:http://git-scm.com/book/en/Git-Branching-Branching-Workflows#Topic-Branches
[console output]:https://help.github.com/articles/github-flavored-markdown#fenced-code-blocks
[verification steps]:https://help.github.com/articles/writing-on-github#task-lists
[reference associated issues]:https://github.com/blog/1506-closing-issues-via-pull-requests
[API]:ainda_nao 
[Module Documentation]: https://github.com/darkcode357/thg-framework/wiki/Generating-Module-Documentation
[Issues]: https://github.com/darkcode357/thg-framework/issues
[THG Slack]: https://www.THG.com/slack
