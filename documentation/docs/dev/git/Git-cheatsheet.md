## Git Cheatsheet (nível de sobrevivência)

Aqui está um conjunto de algumas das coisas mais comuns que você precisa fazer no
seu fluxo de trabalho diário com o Git.

**Dica 1:** você pode obter páginas de manual para qualquer comando git, inserindo um hífen. Como em: "man git-fetch" ou "man git-merge"

**Dica profissional 2:** instale o [pysheeet](https://github.com/crazyguitar/pysheeet)  para ter uma lista de boas paraticas de codigo python

## O que está acontecendo ?

* Em que branch estou? 
* Quais foram os arquivos modificados ?
* Quais são testados, quais não são rastreados etc.?
* Quais foram os arquivos adicionados e modificados
## oque esta acontecendo ? 

* Em que branch estou? Quais arquivos são modificados, quais são testados, quais não são rastreados etc.?
commando ->  `git status`

## Fetch, Pull, and Push

* Receba todas as novas alterações e refs de refs remota
comando->`git fetch`

* Faça uma busca no repositorio git e (se possível) uma mesclagem na ramificação atual(`baixar atualizacoes`)
comando->`git pull`

* Enviar alteracoes para o repositorio usando o push e submetendo a origin/master/(branch especifica) (como o SVN):
comando->`git push origin master`

* alteracoes para uma branch especifica:
    `git push origin your_branch_name`

## Branching

* mostra corrente branches

    `git branch`

* mudar para uma branch especifica

    `git checkout existing_branch_name`

* Crie uma nova branch e mude para ela:

    `git checkout -b new_branch_name`


## Merging and Stashing

* juntar minha branch de trabalho para a branch atual:
    
    `git merge working_branch_name`

* Limpe temporariamente meu desk para que eu possa mudar para outro ramo

    `git stash`

* Recupere minhas coisas gardadas, deixando-as na lista de esconderijos:

    `git stash apply`

* Recupere minhas coisas escondidas, removendo-as da lista:

    `git stash pop`

## History, Conflicts, and Fixing Mistakes

* ver log dos commits:

    `git log`

* Veja quais alterações foram feitas em um determinado commit:

    `git show COMMIT_HASH`

* Veja informações de log mais detalhadas:

    `git whatchanged`

* Livre-se de todas as alterações que fiz desde a última confirmação:
    
    `git reset --hard`

* Livre-se das alterações de apenas um arquivo:

    `git checkout FILENAME`

*Faça HEAD apontar para o estado da base de código a partir de 2 commits atrás:
    `git checkout HEAD^^`

* Corrija um conflito (com a ferramenta gráfica padrão do sistema):

    `git mergetool`

* Reverte um commit (tenha cuidado com mesclagens!):

    `git revert <commit hash>`

* Reverter um commit de um merge:

    `git revert -m<number of commits back in the merge to revert> <hash of merge commit>`
     
(e.g. git revert -m1 4f76f3bbb83ffe4de74a849ad9f68707e3568e16 will revert the first commit back
     in the merge performed at 4f76f3bbb83ffe4de74a849ad9f68707e3568e16)


## Git in Bash

````
function parse_git_branch {
  git branch --no-color 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}
````