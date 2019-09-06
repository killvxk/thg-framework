# Módulos incluídos

Criado por darkcode0x00

À medida que os módulos Metasploit continuam a crescer em número e capacidade, a atual separação das informações dos módulos por tipo se torna mais complicada. A partir do próximo ano, queremos que todos os arquivos relacionados a um módulo (documentos, bibliotecas, fontes, informações de compilação, etc.) vivam o mais próximo possível e sejam o mais hacker possível. Para esse fim, criamos o conceito de "pacotes de módulos" para ajudar a melhorar o isolamento de dependências do módulo e a localização das informações. Esperamos que o formato seja flexível o suficiente para acomodar a ampla gama de módulos que temos e uniforme o suficiente para não causar confusão entre os membros da comunidade e colaboradores. Eventualmente, podemos até empacotar cada módulo separadamente para distribuição.

É incerto se esse formato de pacote suportará ou não o estilo antigo do módulo. Poderia ser feito para funcionar, eu acho, mas exigiria um pouco de esforço e ingenuidade para funcionar corretamente. Por uma questão de simplicidade, descreverei o conceito de pacote como ele se aplica aos módulos externos / coldstone e, em seguida, descreverei possíveis adaptações no final.

## Estrutura do diretório class / plugin

Exemplo de módulo python :

```
thgc create darkcode -t thgclass 
tree --dirsfirst --charset=ascii -F class_name/
class_plugins_name/
|-- docs/
|-- imagens/
|-- requirements/
|   |-- base.txt
|   |-- dev.txt
|   |-- prod.txt
|   `-- test.txt
|-- test_thg_plugin_class/
|   |-- __init__.py
|   |-- pylintrc
|   `-- test_myplugin.py
|-- thg_plugin_class/
|   `-- source/
|       |-- __init__.py
|       |-- myplugin.py
|       `-- pylintrc
|-- thg_plugin_class_example/
|   `-- example.py
|-- build-pyenvs.sh
|-- CHANGELOG.md
|-- LICENSE.md
|-- Pipfile
|-- Pipfile.lock
|-- README.md
|-- setup.cfg
|-- setup.py
|-- tasks.py
`-- tox.init

7 directories, 21 files


```
#plugin
```
thgc create plugins_name -t thgplugin
root@darkcode:/# tree --dirsfirst --charset=ascii -F plugins_name/
plugins_name/
|-- docs/
|-- imagens/
|-- requirements/
|   |-- base.txt
|   |-- dev.txt
|   |-- prod.txt
|   `-- test.txt
|-- test_thg_plugin/
|   |-- __init__.py
|   |-- pylintrc
|   `-- test_myplugin.py
|-- thg_plugin/
|   `-- source/
|       |-- __init__.py
|       |-- pylintrc
|       `-- thg_plugin.py
|-- thg_plugin_example/
|   `-- thg_plugin.py
|-- build-pyenvs.sh
|-- CHANGELOG.md
|-- LICENSE.md
|-- Pipfile
|-- Pipfile.lock
|-- README.md
|-- setup.cfg
|-- setup.py
|-- tasks.py
`-- tox.init

7 directories, 21 files

```
## modulos info

 - O executável principal recebe  o nome do módulo (igual ao diretório)
 - Os arquivo do modulos são todos corelacionados
 - Nós permitiremos vários módulos, tendo interação um com outro, porem não recomendamos essa estrutura de dependencia (por exemplo, integração 2 dois modulos simutaneamente, recomendo submeter a brach master para realaplicao do modulo com dependência multiplas)
 
## Arquivos necessários

Para manter a sobrecarga no mínimo para os hackers que estão desenvolvendo módulos, precisamos minimizar os arquivos que o autor precisará criar, modificar e entender para a maioria das tarefas (atualizado: todos os arquivos que um autor deve criar devem estar diretamente relacionados a determinados e especializados funcionalidade que eles desejam como parte da preparação ou execução de um módulo). O módulo mais mínimo requer apenas que o executável principal esteja presente. Ao carregar os módulos, o framework verá um diretório principal sem certos arquivos esperados e gerará os padrão automaticamente. Esse comportamento pode ser posteriormente aumentado com a adivinhação de quais padrões com base no que está presente no diretório.

 - Se o pyinvoke estiver ausente, o framework irá gerar um que faça referência às tarefas de py compartilhadas.
 - Se o pipenv  estiver ausente e o executável terminar em .py, o framework irá gerar um que dependa das bibliotecas do modulo.
 - Toda essa lógica de geração deve estar disponível no thgscaffolding
## Mantendo tudo perto

Uma das desvantagens do sistema de módulos atual é que todos os arquivos relacionados ao desenvolvimento, documentação e execução de um módulo vivem em locais diferentes. Algumas informações, como dependências, são rastreadas apenas implicitamente ou com perdas no código ou nas especificações de nível superior da estrutura. Isso determina de forma programática o que é um módulo, é direcionado ou requer um código frágil.
### Informações da versão

Todas as informações adicionais de compilação devem ser especificadas como tarefas do módulo desenvolvido. Tanto quanto possível, isso também deve incluir a criação de ambientes IDE, como o Visual Studio. Mesmo que os binários sejam verificados para reduzir os requisitos de tempo de execução (veja abaixo), ainda é inestimável saber como algo foi construído em primeiro lugar.

### Blobs e fontes

As fontes são úteis, deve ser fácil encontrá-las! Agora eles viverão no módulo no diretório src /

Na medida do possível, apenas as fontes devem ser verificadas na árvore. Porém, para plataformas superespecíficas direcionadas a coisas, isso nem sempre é viável (por exemplo, projetos do VisualStudio). Em momentos como esse, o diretório {{data /}} deve ser usado. Como mencionado acima

Blobs ou ativos sem uma fonte de check-in também pertencem a dados /, como imagens ou itens baixados. As coisas para as explorações de clientes para download provavelmente também devem aparecer aqui, como arquivos HTML e JavaScripts estáticos
### Modelos

usando o thgc voce consegue criara modelos de class e modelos de plugins
### Documentos

O diretório docs / conterá os arquivos aos quais o usuário fará referência ao tentar entender o módulo. Isso pode incluir PoCs, descontos, pcaps etc.

### Ferramentas adicionais

Uma vantagem que essa estrutura de diretórios nos oferece é a capacidade de escrever ferramentas melhores para ela do que para a iteração atual dos módulos. Uma desvantagem é que precisamos disso para tornar o formato acessível aos hackers.
### Tarefas de construção compartilhadas

Como todas as tarefas rotineiras orientadas ao módulo serão executadas com tarefas de python, 
precisaremos tornar as ações padrão para essas tarefas o mais inteligentes e reutilizáveis 
possível em diferentes tipos / implementações de módulos. O autor do módulo não deve se preocupar 
em escrever o encanamento de que não precisa (ou é comum) ou mexer com o encanamento que esteja relacionado 
apenas tangencialmente à sua necessidade exclusiva. Para esse fim, devemos ter padrões saudáveis para o {} seguinte, no mínimo:

### Geração de módulos

No mínimo, também precisaremos de ferramentas para criar um módulo quase vazio, logo usamos os thgc