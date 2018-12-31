## THG-FRAMEWORK
# About the project

Project build to be a development and pentesting tool of SO, build using python in the lastest version, currently python 3.7.

# Instalation
Just run this on Terminal:
```
git clone https://github.com/darkcode357/thg-framework.git
cd thg-framework
python
python3 setup.py
```
# Use
To open THGConsole run:
```python
python3 thgconsole.py
```

# Terminal Screenshot
![logo](https://github.com/darkcode357/thg-framework/blob/master/fotos/thg.png)

# Documentation
=> https://darkcode357.github.io/thg-framework/

# How to contribute:
Follow the link bellow with all instructions.
=> https://darkcode357.github.io/thg-framework/contributing/get-started/

# Credits:

| devs          | name nick     |
| ------------- |:-------------:|
| master dev    | darkcode0x00  |

# Future updates
The "[x]" are the commands that is working and the "[]" are the future funcionalities to be applied.

#Commands list:

# Alias Commands

| Command        | Description|
| -------------  |:-------------: |
| - [ ] alias    | create or view an alias. |
| - [ ] del      |  rm |
| - [ ] handler  |  use exploit/multi/handler |

# Core Commands

Command              | Description
| -------------      |:-------------: |
| - [x] show banner  |    Display an awesome thgbanner|
| - [x] show Ip      |   show internal ip|
| - [x] exit         |   Exit the console|
| - [x] unsetg       |  Unsets one or more global variables|
| - [x] help         | Help menu|
| - [x] show history | Show command history|
| - [x] setg         | Sets a global variable to a value|
| - [x] set          | Sets a context-specific variable to a value|
| - [x] exec         | <shell command> <args> Execute a command in a shell|
| - [x] cd           | Change the current working directory|
| - [x] color        | Toggle color|
| - [x] route        | Route traffic through a session V-1base|
| - [x] show version | Show the framework and console library version numbers|
| - [x] quit         | Exit the console|
| - [ ] *connect*    |  Communicate with a host|
| - [ ] *grep*       |  Grep the output of another command|
| - [ ] *load*       | Load a framework plugin|
| - [ ] *save*       | Saves the active datastores|
| - [ ] *sessions*   | Dump session listings and display information about sessions|
| - [x] sleep        | Do nothing for the specified number of seconds|
| - [ ] *spool*      |   Write console output into a file as well the screen|
| - [ ] *unload*     |   Unload a framework plugin|



# Module Commands

Command               |Description
| -------------       |:-------------: |
| - [x] show all      |   show all modules -> (@sys_module)|
| - [x] show creds    |   show creds in db -> (@module_required)|
| - [x] show devices  |  show devices modules -> (@module_required)|
| - [x] show encoders |  show encoders for module -> (@module_required)|
| - [x] show exploits |  show exploit modules -> (@sys_module)|
| - [x] show auxiliary|  show auxiliary modules -> (@sys_module)|
| - [x] show nops     |  show nops modules -> (@sys_module)|
| - [x] show payloads |  show payload modules -> (@sys_module)|
| - [x] show post     |  show post modules -> (@sys_module)|
| - [x] show info     | show info modules -> (@module_required)|
| - [x] show options  | show options in the modules -> (@module_required)|
| - [x] show wordlists| show wordlist in thgconsole date -> (@module_required)|
| - [x] show threads  | View and manipulate background threads -> (@module_required)|
| - [ ] *advanced*    | Displays advanced options for one or more modules -> (@sys_module)|
| - [x] back          | Move back from the current context -> (@sys_module)|
| - [x] show info     | Displays information about one or more modules|
| - [ ] *loadpath*    | Searches for and loads modules from a path -> (@sys_module)|
| - [x] show options  | Displays global options or for one or more modules|
| - [ ] *popm*        | Pops the latest module off the stack and makes it active -> (@sys_module)|
| - [ ] *previous*    | Sets the previously loaded module as the current module -> (@sys_module)|
| - [ ] *pushm*       | Pushes the active or list of modules onto the module stack -> (@sys_module)|
| - [ ] *reload_all*  | Reloads all modules from all defined module paths -> (@sys_module)|
| - [x] search        | Searches module names and descriptions -> (@sys_module)|
| - [x] show          | Displays modules of a given type, or all modules -> (@sys_module)|
| - [x] use           | Selects a module by name -> (@sys_module)|


# Job Commands

Command               |Description
| -------------       |:-------------: |
| - [ ] handler   |        Start a payload handler as job
| - [ ] jobs      |      Displays and manages jobs
| - [ ] kill      |    Kill a job
| - [ ] rename_job|  Rename a job


# Resource Script Commands

Command               |Description
| -------------       |:-------------: |
|- [ ] *makerc*        |Save commands entered since start to a file
|- [ ] *resource*      |Run the commands stored in a file

# Developer Commands

Command               |Description
| -------------       |:-------------: |
|- [ ] *edit*           |    Edit the current module or a file with the preferred editor
|- [x] python_interpreter|  Drop into python  scripting mode
|- [x] log                | Displays framework.log starting at the bottom if possible
|- [ ] *reload_lib*        | Reload one or more library files from specified paths

# Database Backend Commands

Command               |Description
| -------------       |:-------------: |
|- [ ] *db_connect*        |Connect to an existing database
|- [ ] *db_disconnect*     |Disconnect from the current database instance
|- [ ] *db_export*         |Export a file containing the contents of the database
|- [ ] *db_import*         |Import a scan result file (filetype will be auto-detected)
|- [ ] *db_nmap*           |Executes nmap and records the output automatically
|- [ ] *db_rebuild_cache*  |Rebuilds the database-stored module cache
|- [ ] *db_status*         |Show the current database status
|- [ ] *show hosts*         |    List all hosts in the database
|- [ ] *show loot*         |     List all loot in the database
|- [ ] *show notes*       |      List all notes in the database
|- [ ] *show services*   |       List all services in the database
|- [ ] *show vulns*     |        List all vulnerabilities in the database
|- [ ] *show workspace*|         Switch between database workspaces
|- [ ] *show creds*     |    List all credentials in the database


License: BSD-3-clause
