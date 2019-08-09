# Olá Mundo!

Obrigado pelo seu interesse em fazer thg - e, portanto, o
mundo - um lugar melhor! Antes de começar, revise nossa

- [Código de conduta]. Existem várias maneiras de ajudar além de apenas escrever código:
- [Envie bugs e solicitações de recursos] com informações detalhadas sobre o seu problema ou ideia.
- [Ajude os usuários com problemas em aberto] ou [ajude os colegas a testar as solicitações de recebimento recentes].
- [Relate uma vulnerabilidade de segurança no próprio thg] para o Rapid7.
- Envie um módulo atualizado ou novo! Estamos sempre ansiosos por façanhas, scanners e novos  integrações ou recursos. Não sabe por onde começar? Configure um [ambiente de desenvolvimento] e, em seguida, vá até o ExploitDB para procurar por [exploits de prova de conceito] que possam fazer um bom módulo.

# Contribuindo para o thg

Aqui está uma pequena lista de fazer e não fazer para garantir que suas valiosas contribuições realmente façam
no branch master do thg. Se você não se importa em seguir estas regras, sua contribuição
**Será fechado. Desculpa!**

## Contribuições do Código

Continue com o [Guia de estilo do Ruby] e use o [Rubocop] para encontrar problemas comuns de estilo.
* **Faca** siga a [regra 50/72] para mensagens de commit do Git.
* **Faca** licencie seu código como BSD 3-clause, BSD 2-clause, ou MIT.
* **Crie** um [tópico] para trabalhar em vez de trabalhar diretamente no `mestre`.
  Isso ajuda a proteger o processo, garante que os usuários estejam cientes dos commits no branch sendo considerado para mesclagem,
  permite um local para que mais commits sejam oferecidos sem se misturar com outras mudanças de contribuidores,
  e permite que os contribuintes façam progresso enquanto um PR ainda está sendo revisado.


### pedidos de extração

* **Escreva** WIP em seu PR e / ou abra um [rascunho de PR] se enviar ** código de trabalho ** ainda não finalizado.
* **Do** direcione sua solicitação de recebimento para a ** ramificação principal **.
* **Do** especifica um título descritivo para facilitar a busca por sua solicitação pull.
* **Do** inclui [saída do console], especialmente para efeitos observáveis ​​em `thgcli`.
* **Do** listar [etapas de verificação] para que seu código seja testável.
* **Do** [questões associadas à referência] na sua descrição de solicitação pull.
* **Não** deixe sua descrição de solicitação pull em branco.
* **Não** abandone seu pedido pull. Ser receptivo nos ajuda a posicionar seu código mais rapidamente.

O pedido de pull [PR # 9966] é um bom exemplo a seguir.

#### Novos módulos

* **Defina** `thgfix` para corrigir quaisquer erros ou avisos que surjam como um [gancho de pré-consolidação].
* **Do** use os diversos mixin [API] s do módulo.
* **Não** inclui mais de um módulo por solicitação pull.
* **Do** inclui instruções sobre como configurar o ambiente ou software vulnerável.
* **Do** inclui [Documentação do Módulo] mostrando exemplos de execuções.
* **Não** envie novos [scripts]. Scripts são enviados como exemplos para automatizar tarefas locais e
  qualquer coisa "séria" pode ser feita com post modules e exploits locais.

#### Código da biblioteca

* **Faça** testes de [RSpec] - até mesmo a menor alteração em uma biblioteca pode quebrar o código existente.
  **Siga** [Better Specs] - é como o guia de estilo para especificações.
* **Faça** escreva a documentação [YARD] - isto torna mais fácil para as pessoas usarem o seu código.
* **Não** conserte muitas coisas em um único pedido. Pequenas correções são mais fáceis de validar.

#### Correções de bugs

* **Do** inclui etapas de reprodução na forma de etapas de verificação.
* **Faça** link para qualquer [Issues] correspondente no formato de 'See # 1234` na sua descrição de commit.

## Relatório de erros

Por favor, relate as vulnerabilidades no software do darkcode0x00 diretamente para security@darkcode0x00.com. Para mais informações sobre nossa política de divulgação e a abordagem do darkcode0x00 para divulgação coordenada, [head over here] (https://www.rapid7.com/security).

## Ao relatar problemas do thg:
**Faça** uma descrição detalhada do seu bug e use um título descritivo.
**Faca** inclui etapas de reprodução, rastreamentos de pilha e qualquer coisa que possa nos ajudar a corrigir seu bug.
**Não** arquive relatórios duplicados; pesquise seu bug antes de preencher um novo relatório.

Se você precisar de mais orientação, fale com o corpo principal de contribuidores de código aberto sobre nossos
[thg Discord] .

Por fim, **obrigado** por aproveitar alguns momentos para ler até aqui! Você já está bem à frente do
curva, então continue assim!

