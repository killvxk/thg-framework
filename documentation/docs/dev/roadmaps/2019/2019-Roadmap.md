

# THG Roadmap 2019 

A partir de 2019, forneceremos um roteiro aberto para definir nossas metas para o ano. As metas são baseadas em muitas discussões que tivemos no nucleo de desenvolvimento `thg-xcode-dev` com usuários, desenvolvedores e clientes. A intenção é fornecer foco para os principais desenvolvedores e colaboradores, para que possamos trabalhar juntos em direção a uma visão comum de como queremos que o thg evolua.

Este ano, os temas do THG são modularidade, ,desenvolvimento do nucleo,estabilidade,modelos de class

O THG cresceu organicamente ao longo dos anos em um projeto muito grande, combinando  os módulos, cargas úteis, junto a grande  banco de dados, interação do usuário e muito mais em um único aplicativo monolítico. Embora o design tenha nos servido bem, ele atingiu alguns limites de manutenção e agilidade. Enquanto continuamos a refatorar, aprimorar e reorganizar o THG diariamente, aprimoramentos em larga escala se tornam cada vez mais difíceis e destacam a fragilidade no sistema geral, devido ao seu design altamente interdependente.

Queremos permitir que os usuários contribuam sem esforço para as partes do THG em que estão interessados ​​e possam reutilizar o código, tanto dentro como fora do projeto. As restrições de idioma e licenciamento apresentaram barreiras para os usuários, reais e imaginários. Python, Go, C # e outras linguagens estão influenciando predominantemente a comunidade infosec. Gostaríamos de poder acolher mais desenvolvedores, pesquisadores e ferramentas no ecossistema do THG, aproveitando o melhor da categoria e evitando a `síndrome não inventada` aqui sempre que possível.

Em resumo, queremos desenvolver serviços reutilizáveis, modulares e confiáveis ​​para permitir que pesquisadores, testadores , estudantes e equipes vermelhas trabalhem eficientemente, tenham acesso às mais recentes tecnologias e técnicas e continuem a crescer a comunidade THG.



## O roteiro

 * O back-end do modelo de dados do TGH deve ser separado em seu próprio projeto. Os planos incluem um serviço de dados que fornece uma interface RESTful, uma visualização orientada a eventos e  suporte a co-rotinas, desempenho aprimorado e fácil interoperabilidade direta com outras ferramentas.

 * O tratamento de sessões deve poder operar independentemente da estrutura, permitindo que os usuários compartilhem sessões e permitindo que os servidores tenham o melhor desempenho, a confiabilidade e o menor peso possível. Já começamos um projeto chamado 'xcode-socket-0x00', que é a primeira geração desse design. Uma vez concluído, a integração direta com outras estruturas também deve ser possível.

 * O THG deve suportar sessões assíncronas. Atualmente, muitos testadores usam estruturas assíncronas, como o Empire, para manter uma persistência leve ou pontos de apoio em uma rede, e depois precisam interagir com a CybersX nas sessões interativas. Gostaríamos de poder suportar perfeitamente os dois modos de operação, incluindo a capacidade de executar módulos pós-exploração e módulos sobre pivôs de maneira assíncrona.

 * O THG deve suportar a execução de exploração e módulos auxiliares em um modo isolado. Estão em andamento planos para oferecer suporte a uma API de módulo RPC/RESTFULL para a estrutura do THG, fornecendo serviços principais como carga útil e manipulação de sessões, roteamento de rede, relatórios e registros. Os módulos são executados como processos filhos no THG e são carregados apenas na memória, conforme necessário. A rede do ponto de vista do módulo será gerenciada por meio do suporte a proxy SOCKS5, conectando o ambiente filho ou chamadas remotas à API, removendo amplamente a necessidade de objetos de SOCKETS especialmente criados ou alterações nas bibliotecas de protocolos de terceiros. Os módulos, quando escritos para a API THG, podem até ser testados e usados ​​independentemente da estrutura completa do THG .

Além dessas metas principais, também gostaríamos de explorar:

* Gostaríamos de implementar pelo menos o suporte do servidor para SMB 2.0, tanto para compartilhar arquivos quanto para comunicações de pipe nomeado.
 * * A otimização do medidor do medidor do Windows * em breve substituirá o medidor do POSIX original, o que reduzirá o tamanho do medidor do Windows. Mudar do OpenSSL para o suporte nativo ao SChannel simplificará e reduzirá o indicador do medidor do Windows, permitindo focar no que ele suporta melhor.
 * * Pesquisa de roteador e IoT * Gostaríamos de continuar a pesquisa e suporte para exploração de dispositivos incorporados e suporte de primeira classe para ambientes com recursos limitados.
 * * Modernizando a geração de carga útil * Estamos investigando a possibilidade de integração com cadeias de ferramentas de terceiros para a montagem e compilacao de  C, .NET, Java, dinamicamente, facilitando ao usuário a aquisição e o uso das ferramentas, fornecendo o primeiro Suporte a várias arquiteturas e plataformas.