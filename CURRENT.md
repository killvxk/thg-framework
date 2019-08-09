O desenvolvimento ativo do thg às vezes promove mudanças agressivas.
As integrações com ferramentas de terceiros, bem como o uso geral, podem mudar rapidamente
de dia para dia. Algumas das etapas para lidar com grandes mudanças serão
documentado aqui. Continuaremos a manter a ramificação do thg  1.x até
thg 2.0 for lançado.


O thg  armazena  os metadados do módulo em um banco de dados mongodb.
armazenando-o em um arquivo de cache em seu diretório local de configuração ~/.thg Isso tem um
número de vantagens:

 * Pesquisas rápidas se você tem o banco de dados ativado ou não (modo de pesquisa lenta(ler json))
 * Tempo de carregamento mais rápido para o THG, o cache carrega mais rapidamente
 * Os dados dos módulos privados não seram enviados para um banco de dados compartilhado, sem colisões
 * Adicionar ou excluir módulos não exibe mais as mensagens de erros {encontradas no início do THG}
 * Consumo de memória reduzido

Código que lê diretamente o banco de dados thg para suporte `NoSQL` 