# Welcome to THG-FRAMEWORK

## introduction to thg_FRAMEWORK

novo sistema de exploracao e associacao de dados, voltados para comprovar a tese de desenvolvimento de uma versao alternativa do metasploit feito em python

```

        ===================[ thgconsole 2.0.1-dev ]===================

        + -- --=[THGEF   : The Hacker Group Exploitation Framework]=-- -- +    
        + -- --=[Code by : Darkcode                               ]=-- -- + 
        + -- --=[Codename: 0box                                ]=-- -- + 
        + -- --=[Homepage: https://www.facebook.com/darckode0x00/ ]=-- -- + 
        + -- --=[youtube : darkcode programming                   ]=-- -- + 

        ===================[ thgconsole-pc ]========================

        + -- --=[system  => Linux              ]=-- -- + 
        + -- --=[machine => x86_64             ]=-- -- +      
        + -- --=[gcc     => 8.3.0              ]=-- -- +
        + -- --=[python  => 3.7                ]=-- -- +
        + -- --=[net     => THG_Online         ]=-- -- +
        + -- --=[ip      => 192.168.23.102     ]=-- -- +
        + -- --=[mac     => 90:cd:b6:a4:64:e1  ]=-- -- +

        ===================[ thgconsole-info   ]========================
        ===================[ thgconsole-config ]========================
        + -- --=[DB_STATUS =>on                ]=-- -- +
                

thg-console > 
```
#thg commandos
```
thg-console > help -v

Documented commands (type help <topic>):

Core Command
================================================================================
banner              Print thg-console banner
exec                <shell thg_command> <args> Execute a thg_command in a shell
exit                Exit the console
ip                  show ip
version             show version

Database Backend Commands
================================================================================
db_rebuild          Rebuild database for search
reload              reload the chose module

Module Command
================================================================================
back                Clear module that chose
check               Execute module check
exploit             Execute module exploit
listmod             List all modules
run                 alias to exploit
search              Search modules
set                 Set module option value/ set program config
show                Display module information
use                 Chose a module

Other
================================================================================
alias               Manage aliases
edit                Edit a file in a text editor
help                List available commands or provide detailed help for a specific command
history             View, run, edit, save, or clear previously entered commands
ipy                 Enter an interactive IPython shell
load                Run commands in script file that is encoded as either ASCII or UTF-8 text
macro               Manage macros
py                  Invoke Python command or shell
pyscript            Run a Python script file inside the console
quit                Exit this application
shell               Execute a command as if at the OS prompt
shortcuts           List available shortcuts

thg-console > 
```

#Core Command
```
banner              Print thg-console banner
exec                <shell thg_command> <args> Execute a thg_command in a shell
exit                Exit the console
ip                  show ip
version             show version
```

# Database Backend Commands
```
db_rebuild          Rebuild database for search
reload              reload the chose module
```
#Module Command
```
back                Clear module that chose
check               Execute module check
exploit             Execute module exploit
listmod             List all modules
run                 alias to exploit
search              Search modules
     *search name, 
     *module_name, 
     *description, 
     *author, 
     *disclosure_date, 
     *service_name, 
     *service_version, 
     *check

set                 Set module option value/ set program config
show                Display module information

    *info display info mode       
    *missing display missing options    
    *options display options for mods

use                 Chose a module
```
# aux
```
alias Manage aliases
Usage: alias [-h] {create, delete, list} ...

Manage aliases

An alias is a command that enables replacement of a word by another string.

optional arguments:
  -h, --help            show this help message and exit

sub-commands:
  {create, delete, list}
    create              create or overwrite an alias
    delete              delete aliases
    list                list aliases




edit Edit a file in a text editor
Usage: edit [-h] [file_path]

Edit a file in a text editor

The editor used is determined by a settable parameter. To set it:

  set editor (program-name)

positional arguments:
  file_path   path to a file to open in editor

optional arguments:
  -h, --help  show this help message and exit


help List available commands or provide detailed help for a specific command
Usage: help [-h] [-v] [command] ...

List available commands or provide detailed help for a specific command

positional arguments:
  command        command to retrieve help for
  subcommand     sub-command to retrieve help for

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  print a list of all commands with descriptions of each


history View, run, edit, save, or clear previously entered commands
Usage: history [-h] [-r | -e | -o FILE | -t TRANSCRIPT | -c] [-s] [-x] [-v]
               [arg]

View, run, edit, save, or clear previously entered commands

positional arguments:
  arg                   empty               all history items
                        a                   one history item by number
                        a..b, a:b, a:, ..b  items by indices (inclusive)
                        string              items containing string
                        /regex/             items matching regular expression

optional arguments:
  -h, --help            show this help message and exit
  -r, --run             run selected history items
  -e, --edit            edit and then run selected history items
  -o, --output-file FILE
                        output commands to a script file, implies -s
  -t, --transcript TRANSCRIPT
                        output commands and results to a transcript file,
                        implies -s
  -c, --clear           clear all history

formatting:
  -s, --script          output commands in script format, i.e. without command
                        numbers
  -x, --expanded        output fully parsed commands with any aliases and
                        macros expanded, instead of typed commands
  -v, --verbose         display history and include expanded commands if they
                        differ from the typed command


ipy                 Enter an interactive IPython shell
load                Run commands in script file that is encoded as either ASCII or UTF-8 text
macro               Manage macros
py                  Invoke Python command or shell
pyscript            Run a Python script file inside the console
quit                Exit this application
shell               Execute a command as if at the OS prompt
shortcuts           List available shortcuts
```