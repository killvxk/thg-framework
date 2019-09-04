# Módulos incluídos

Criado por darkcode0x00

À medida que os módulos Metasploit continuam a crescer em número e capacidade, a atual separação das informações dos módulos por tipo se torna mais complicada. A partir do próximo ano, queremos que todos os arquivos relacionados a um módulo (documentos, bibliotecas, fontes, informações de compilação, etc.) vivam o mais próximo possível e sejam o mais hacker possível. Para esse fim, criamos o conceito de "pacotes de módulos" para ajudar a melhorar o isolamento de dependências do módulo e a localização das informações. Esperamos que o formato seja flexível o suficiente para acomodar a ampla gama de módulos que temos e uniforme o suficiente para não causar confusão entre os membros da comunidade e colaboradores. Eventualmente, podemos até empacotar cada módulo separadamente para distribuição.

É incerto se esse formato de pacote suportará ou não o estilo antigo do módulo. Poderia ser feito para funcionar, eu acho, mas exigiria um pouco de esforço e ingenuidade para funcionar corretamente. Por uma questão de simplicidade, descreverei o conceito de pacote como ele se aplica aos módulos externos / coldstone e, em seguida, descreverei possíveis adaptações no final.

## Estrutura do diretório

Exemplo de módulo python :

```
tree --dirsfirst --charset=ascii -F python-package-template/
python-package-template/
|-- docs/
|   |-- _static/
|   |-- authors.rst
|   |-- changelog.rst
|   |-- conf.py
|   |-- index.rst
|   |-- license.rst
|   `-- Makefile
|-- src/
|   `-- python-package-template/
|       |-- __init__.py
|       `-- skeleton.py
|-- tests/
|   |-- conftest.py
|   `-- test_skeleton.py
|-- AUTHORS.rst
|-- CHANGELOG.rst
|-- LICENSE.txt
|-- README.rst
|-- requirements.txt
|-- setup.cfg
`-- setup.py

5 directories, 17 files


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

## Keeping it all close

One of the drawbacks of the current module system is that all the files related to the development, documentation, and execution of a module live in different places. Some information, like dependencies, is only tracked implicitly or lossily in code or in the top-level specifications of framework. This makes programmatically determining what a module is, targets, or requires fraught with fragile code.

### Metadata

The metadata will be kept in JSON in a file (or several, see my uncertainties above) that is built by rake. Keeping the metadata cached per-module gives us several capabilities. First, updates look more logical in commits, and the files can be updated as part of the standard PR/landing process. Next, dependency tracking of when the metadata needs to be updated can be offloaded to standard build tool capabilities.

Because invoking rake has overhead, any metadata that exists should be considered correct during initial module discovery. Any modules without metadata should then have it generated via rake. Next, every module should have its metadata building task run to (and stale metadata replaced) ensure correctness. If a module is use'd before this process completes, it must have it metadata refreshed via rake if needed as part of the loading process. Since modules are independent, the whole discovery/refreshing process is parallelizable, reducing wall time.

In addition to the information we currently cache, we will want to cache any information a user might see or want to know so that, if the cached metadata is more recent than any module files, nothing has to be built or run to use the module. Notably, this includes options and module archetype (which in the future directly map options for user convince, vs the shim approach take today).

### Build info

All additional build info should be specified as tasks in the module Rakefile. As much a possible, this should also include building with IDE environments, like Visual Studio. Even if the binaries are checked in to reduce runtime requirements (see below), it is still invaluable to know how something was built in the first place.

### Blobs and sources

Sources are handy, it should be easy to find them! Now they will live in the module in the src/ directory. Here the Rakefile can easily find them and transform them into the beautiful exploitation resources they were meant to be.

As much as possible, only sources should be checked into the tree. For super-specific platform targeting things though, that's not always feasible (eg. VisualStudio projects). It's times like these that the {{data/}} directory should be used. As mentioned above, the Rakefile should still be able to build the thing given the correct environment.

Blobs or assets without a checked-in source also belong in data/, like images or downloaded things. Things for client exploits to download should probably also go in here, like HTML files and static JavaScripts.

### Templates

Modules that use a large literal interspersed with runtime data should use the templates/ directory to store templates. ERB should be used for printable data by Ruby, and equivalents for other languages (DTL, mustache, etc.). Binary data should maybe be blobs with accompanying offset listings?

### Docs

The docs/ directory will contain the files that a user will reference when trying to understand module. This may include PoCs, markdown, pcaps, etc. The HTML we currently show to users would be generated from the module and files here using rake tasks.

### Additional tooling

One advantage that this directory structure gives us is the ability to write better tooling for it than we have for the current iteration of modules. One downside is that we will need it to in order to make the format accessible to hackers.

### Shared build tasks

Because all routine module-oriented tasks will be preformed with rake tasks, we will need to make the default actions for these tasks as intelligent and reusable as possible across different module types/implementations. A module author should not have to worry about writing plumbing they do not need (or is common) or messing with plumbing that is only tangentially related to their unique need. To that end, we should have sane defaults for the following at a minimum:

```
rake run -- Start module, hook up stdin/stdout to JSON-RPC
rake metadata -- Generate metadata JSON
rake tidy:code -- Run tidiness checks against the code
rake tidy:metadata -- Run tidiness checks against the metadata
rake doc:text -- Combine all docs into a plain-text, human readable thing
rake doc:html -- Similar to today's info -d
rake deps -- Install dependencies local to the current user, if possible
rake deps:check -- Check to see if a module can likely be run in the current environment
rake build -- Build files that need it, defaults: src/FILE.s => data/FILE (extracted from exe format), ...?
rake clean -- Remove generated files
rake clobber -- Reset to pristine, checked-out state
```

### Module generation

At the very least, we will also need tooling to create a mostly-empty but runnable module so that an author knows what to poke when writing. This skeleton can be augmented by questions that can help us use different archetypes, like payload vs. remote, or Ruby vs. Python. These commands could also point the author to relevant module writing articles/documentation.

### For classic modules

The biggest differences for classic modules are metadata generation and running. These can be accomplished with rake tasks, but it would involve starting up a whole framework instance for each module run. For efficiency, we will need to signal to framework to treat the module specially, perhaps having rake deps:check output/return a specific value when the module needs to be run inside of framework. Metadata would then be dumped directly from the framework loader, and instead of rake run, the classic module loader/runner would be run much as it is today. We will probably want to keep the rake tasks for these things for when we don't already have a framework instance handy.