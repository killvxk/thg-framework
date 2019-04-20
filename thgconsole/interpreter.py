from __future__ import print_function
import getopt
import atexit
import itertools
import os
import sys
from glob import glob
import traceback
import socket, platform
from collections import Counter
from colorama import Fore
from future.builtins import input
from time import sleep
import shutil
##shutil
##DB > THG
##
#from thgconsole.core.db.insert_db import DBSession,check

##
##mods
import psutil
from psutil._common import *


from thgconsole.config.Version import __codenome__, __version__

from thgconsole.core.exploit.exceptions import THGtException
from glob import glob
from thgconsole.core.exploit.utils import (
    index_extra_modules,
    index_modules,
    pythonize_path,
    humanize_path,
    import_exploit,
    stop_after,
    module_required,
    MODULES_DIR,
    WORDLISTS_DIR,
)
from thgconsole.config.info_init import thg_add_init
from thgconsole.core.exploit.printer import (
    print_info,
    print_success,
    print_error,
    print_status,
    print_table,
    pprint_dict_in_order,
    PrinterThread,
    printer_queue
)
from thgconsole.core.exploit.exploit import GLOBAL_OPTS
from thgconsole.core.exploit.payloads import BasePayload

import readline


def is_libedit():
    return "libedit" in readline.__doc__


class THGBaseInterpreter(object):
    history_file = os.path.expanduser("~/.history")
    history_length = 100
    global_help = ""
    def __init__(self):
        self.setup()
        self.banner = ""
    def setup(self):
        """ Initialization of third-party libraries

        Setting interpreter history.
        Setting appropriate completer function.

        :return:
        """
        if not os.path.exists(self.history_file):
            with open(self.history_file, "a+") as history:
                if is_libedit():
                    history.write("_HiStOrY_V2_\n\n")

        readline.read_history_file(self.history_file)
        readline.set_history_length(self.history_length)
        atexit.register(readline.write_history_file, self.history_file)

        readline.parse_and_bind("set enable-keypad on")

        readline.set_completer(self.complete)
        readline.set_completer_delims(" \t\n;")
        if is_libedit():
            readline.parse_and_bind("bind ^I rl_complete")
        else:
            readline.parse_and_bind("tab: complete")
    def parse_line(self, line):
        """ Split line into thg_command and argument.

        :param line: line to parse
        :return: (thg_command, argument)
        """
        thg_command, _, arg = line.strip().partition(" ")
        return thg_command, arg.strip()
    @property
    def THGprompt(self):
        """ Returns THGprompt string """
        return ">>>"
    def get_thg_command_handler(self, thg_command):
        """ Parsing thg_command and returning appropriate handler.

        :param thg_command: thg_command
        :return: thg_command_handler
        """
        try:
            thg_command_handler = getattr(self, "thg_command_{}".format(thg_command))
        except AttributeError:
            raise THGtException("Unknown thg_command: '{}'".format(thg_command))

        return thg_command_handler
    def THGstart(self):
        """ THGconsole main entry point. Starting interpreter loop. """
        # thgvoz.load()
        # DB_CONTROLER.DB.Create_DB()
        print_info(self.banner)
        printer_queue.join()
        while True:
            try:
                thg_command, args = self.parse_line(input(self.THGprompt))
                if not thg_command:
                    continue
                thg_command_handler = self.get_thg_command_handler(thg_command)
                thg_command_handler(args)
            except THGtException as err:
                print_error(err)
            except EOFError:
                print_info()
                print_status("thgconsole stopped")
                break
            except KeyboardInterrupt:
                print_info()
            finally:
                printer_queue.join()
    def complete(self, text, state):
        """Return the next possible completion for 'text'.

        If a thg_command has not been entered, then complete against thg_command list.
        Otherwise try to call complete_<thg_command> to get list of completions.
        """
        if state == 0:
            original_line = readline.get_line_buffer()
            line = original_line.lstrip()
            stripped = len(original_line) - len(line)
            start_index = readline.get_begidx() - stripped
            end_index = readline.get_endidx() - stripped

            if start_index > 0:
                cmd, args = self.parse_line(line)
                if cmd == "":
                    complete_function = self.default_completer
                else:
                    try:
                        complete_function = getattr(self, "complete_" + cmd)
                    except AttributeError:
                        complete_function = self.default_completer
            else:
                complete_function = self.raw_thg_command_completer

            self.completion_matches = complete_function(text, line, start_index, end_index)

        try:
            return self.completion_matches[state]
        except IndexError:
            return None
    def thg_commands(self, *ignored):
        """ Returns full list of interpreter thg_commands.

        :param ignored:
        :return: full list of interpreter thg_commands
        """
        return [thg_command.rsplit("_").pop() for thg_command in dir(self) if thg_command.startswith("thg_command_")]
    def raw_thg_command_completer(self, text, line, start_index, end_index):
        """ Complete thg_command w/o any argument """
        return [thg_command for thg_command in self.suggested_thg_commands() if thg_command.startswith(text)]
    def default_completer(self, *ignored):
        return []
    def suggested_thg_commands(self):
        """ Entry point for intelligent tab completion.

        Overwrite this method to suggest suitable thg_commands.

        :return: list of suitable thg_commands
        """
        return self.thg_commands()


class THGtInterpreter(THGBaseInterpreter):
    history_file = os.path.expanduser("~/.THG_history")
    global_help = """
\033[0;32mGlobal thg_commands:

#Alias Commands
==============

Command       Description
-------       -----------
#alias         create or view an alias.
#del           rm
#handler       use exploit/multi/handler

System command
==============
    Command             Description
    -------             -----------
    battery            show battery info
    free              show mmr/swp info
    killall           kill pid
    netstat           show connect
    pmap              show structure pid
    procsmem          show command line proc info 
    pstree            show process tree
    temperatures      show hardware temperature
    who               list/show current user
    disk_usage        show devices info
    fans              show RPM
    ifconfig          show config network
    meminfo           show memore info
    nettop            show netconect
    procinfo          show procinfo
    ps                show process
    sensors           show hardwares sensors
    top               show process

Core Commands
=============

    Command       Description
    -------       -----------
    show banner    Display an awesome thgbanner
    show Ip        show internal ip 
    exit           Exit the console
    unsetg         Unsets one or more global variables
    help           Help menu
    show history   Show thg_command history
    setg           Sets a global variable to a value
    set            Sets a context-specific variable to a value
    exec           <shell thg_command> <args> Execute a thg_command in a shell
    cd             Change the current working directory
    color          Toggle color
    route          Route traffic through a session V-1base
    show version   Show the framework and console library version numbers
    quit           Exit the console
    #connect       Communicate with a host
    #grep          Grep the output of another thg_command
    #load          Load a framework plugin
    #save          Saves the active datastores
    #sessions      Dump session listings and display information about sessions
    sleep         Do nothing for the specified number of seconds
    #spool         Write console output into a file as well the screen
    #unload        Unload a framework plugin



#Module Commands
===============

    #Command        Description
    -------        -----------
    show all       show all modules {red}->{magent} (@sys_module){Blue}{grn}{grn}
    show creds     show creds in db {red}->{Blue} (@module_required){Blue}{grn}{grn}
    show devices   show devices modules {red}->{Blue} (@module_required){Blue}{grn}{grn}
    show encoders  show encoders for module {red}->{Blue} (@module_required){Blue}{grn}{grn}
    show exploits  show exploit modules {red}->{magent} (@sys_module){Blue}{grn}{grn}   
    show auxiliary show auxiliary modules {red}->{magent} (@sys_module){Blue}{grn}{grn}
    show nops      show nops modules {red}->{magent} (@sys_module){Blue}{grn}{grn}
    show payloads  show payload modules {red}->{magent} (@sys_module){Blue}{grn}{grn}
    show post      show post modules {red}->{magent} (@sys_module){Blue}{grn}{grn}
    show info      show info modules {red}->{Blue} (@module_required){Blue}{grn}{grn}
    show options   show options in the modules {red}->{Blue} (@module_required){Blue}{grn}{grn}
    show wordlists show wordlist in thgconsole date {red}->{Blue} (@module_required){Blue}{grn}{grn}
    show threads   View and manipulate background threads {red}->{Blue} (@module_required){Blue}{grn}{grn}
    #advanced      Displays advanced options for one or more modules {red}->{magent} (@sys_module){Blue}{grn}{grn}
    back           Move back from the current context {red}->{magent} (@sys_module){Blue}{grn}{grn}
    show info      Displays information about one or more modules
    #loadpath      Searches for and loads modules from a path {red}->{magent} (@sys_module){Blue}{grn}{grn}
    options        Displays global options or for one or more modules
    #popm          Pops the latest module off the stack and makes it active {red}->{magent} (@sys_module){Blue}{grn}{grn}
    #previous      Sets the previously loaded module as the current module {red}->{magent} (@sys_module){Blue}{grn}{grn}
    #pushm         Pushes the active or list of modules onto the module stack {red}->{magent} (@sys_module){Blue}{grn}{grn}
    #reload_all    Reloads all modules from all defined module paths {red}->{magent} (@sys_module){Blue}{grn}{grn}
    search         Searches module names and descriptions {red}->{magent} (@sys_module){Blue}{grn}{grn}
    show           Displays modules of a given type, or all modules {red}->{magent} (@sys_module){Blue}{grn}{grn}
    use            Selects a module by name {red}->{magent} (@sys_module){Blue}{grn}{grn}


#Job Commands
============

#Command       Description
-------       -----------
#handler       Start a payload handler as job
#jobs          Displays and manages jobs
#kill          Kill a job
#rename_job    Rename a job


#Resource Script Commands
========================

#Command       Description
-------       -----------
#makerc        Save thg_commands entered since start to a file
#resource      Run the thg_commands stored in a file

#Developer Commands
==================

#Command       Description
-------       -----------
#edit               Edit the current module or a file with the preferred editor
python_interpreter  Drop into python  scripting mode
log                 Displays framework.log starting at the bottom if possible
#reload_lib         Reload one or more library files from specified paths

#Database Backend Commands
=========================

#Command           Description
-------           -----------
#db_connect        Connect to an existing database
#db_disconnect     Disconnect from the current database instance
#db_export         Export a file containing the contents of the database
#db_import         Import a scan result file (filetype will be auto-detected)
#db_nmap           Executes nmap and records the output automatically
#db_rebuild_cache  Rebuilds the database-stored module cache
#db_status         Show the current database status
#hosts             List all hosts in the database
#loot              List all loot in the database
#notes             List all notes in the database
#services          List all services in the database
#vulns             List all vulnerabilities in the database
#workspace         Switch between database workspaces


Credentials Backend Commands
============================

Command       Description
-------       -----------
#creds         List all credentials in the database
    """.format(Blue=Fore.CYAN, grn=Fore.GREEN, red=Fore.RED, yl=Fore.YELLOW, magent=Fore.MAGENTA)
    module_help = """
    \033[1;34mModule thg_commands:
    run                                 Run the selected module with the given options
    back                                De-select the current module
    set <option name> <option value>    Set an option for the selected module
    setg <option name> <option value>   Set an option for all of the modules
    unsetg <option name>                Unset option that was set globally
    show [info|options|devices]         Print information, options, or target devices for a module
    check                               Check if a given target is vulnerable to a selected module's exploit"""
    def __init__(self, extra_package_path=False):
        super(THGtInterpreter, self).__init__()
        PrinterThread().start()

        self.current_module = None
        self.raw_THGprompt_template = None
        self.module_THGprompt_template = None
        self.THGprompt_hostname = "\033[0;32mPWN"
        self.show_sub_thg_commands = sorted(("info",
                                         "ip",
                                         "history",
                                         "options",
                                         "devices",
                                         "all",
                                         "auxiliary",
                                         "encoders",
                                         "exploits",
                                         "evasion",
                                         "nops",
                                         "payloads",
                                         "post",
                                         "wordlists",
                                         "banner",
                                         "version"
                                         ))

        self.iptables_sub_thg_commands = sorted(("info",
                                             "ip",
                                             "history",
                                             "options",
                                             "devices",
                                             "all",
                                             "auxiliary",
                                             "encoders",
                                             "exploits",
                                             "evasion",
                                             "nops",
                                             "payloads",
                                             "post",
                                             "wordlists",
                                             "banner",
                                             "version"
                                             ))
        self.global_thg_commands = sorted(["use",
                                       "exec",
                                       "help",
                                       "exit",
                                       "show",
                                       "search",
                                       "python_interpreter",
                                       "shell",
                                       "cd",
                                       "color",
                                       "route",
                                       "quit",
                                       "sleep",
                                       "iptables",
                                       "battery"

                                       ])
        self.module_thg_commands = ["run", "back", "set ", "setg ", "check"]
        self.module_thg_commands.extend(self.global_thg_commands)
        self.module_thg_commands.sort()
        self.extra_modules_dir = None
        self.extra_modules_dirs = None
        self.extra_modules = []
        self.extra_package_path = extra_package_path
        self.import_extra_package()
        self.modules = index_modules()
        self.modules += self.extra_modules
        self.modules_count = Counter()
        self.modules_count.update([module.split('.')[0] for module in self.modules])
        self.main_modules_dirs = [module for module in os.listdir(MODULES_DIR) if not module.startswith("__")]

        self.__parse_THGprompt()

        self.ran = """\033[1;31m████████╗██╗  ██╗███████╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗      ██████╗ ██████╗  ██████╗ ██╗   ██╗██████╗ 
╚══██╔══╝██║  ██║██╔════╝    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ██╔════╝ ██╔══██╗██╔═══██╗██║   ██║██╔══██╗
   ██║   ███████║█████╗      ███████║███████║██║     █████╔╝ █████╗  ██████╔╝    ██║  ███╗██████╔╝██║   ██║██║   ██║██████╔╝
   ██║   ██╔══██║██╔══╝      ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗    ██║   ██║██╔══██╗██║   ██║██║   ██║██╔═══╝ 
   ██║   ██║  ██║███████╗    ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║    ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║     
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     
        \033[1;34m"""
        self.banner = """
{CYAN}==================={GREEN}[ thgconsole {version} ]{GREEN}{CYAN}===================

{YELLOW}+ -- --=[{RED}THGEF   :{MAGENTA} The Hacker Group Exploitation Framework{RED}{YELLOW}]=-- -- +    
{YELLOW}+ -- --=[{RED}Code by :{MAGENTA} Darkcode                               {RED}{YELLOW}]=-- -- + 
{YELLOW}+ -- --=[{RED}Codename:{MAGENTA} {codenome}                                {RED}{YELLOW}]=-- -- + 
{YELLOW}+ -- --=[{RED}Homepage:{MAGENTA} https://www.facebook.com/darckode0x00/ {RED}{YELLOW}]=-- -- + 
{YELLOW}+ -- --=[{RED}youtube :{MAGENTA} darkcode programming                   {RED}{YELLOW}]=-- -- + 

{CYAN}==================={GREEN}[ thgconsole-pc ]{GREEN}{CYAN}========================

{YELLOW}+ -- --=[{RED}system  =>{MAGENTA} {os}             {RED}{YELLOW}]=-- -- + 
{YELLOW}+ -- --=[{RED}machine =>{MAGENTA} {machine}            {RED}{YELLOW}]=-- -- +      
{YELLOW}+ -- --=[{RED}gcc     =>{MAGENTA} {gccv}             {RED}{YELLOW}]=-- -- +
{YELLOW}+ -- --=[{RED}python  =>{MAGENTA} {python}               {RED}{YELLOW}]=-- -- +
{YELLOW}+ -- --=[{RED}net     =>{MAGENTA} {net}        {RED}{YELLOW}]=-- -- +
{YELLOW}+ -- --=[{RED}ip      =>{MAGENTA} {ip}       {RED}{YELLOW}]=-- -- +
{YELLOW}+ -- --=[{RED}mac     =>{MAGENTA} {mac} {RED}{YELLOW}]=-- -- +

{CYAN}==================={GREEN}[ thgconsole-info ]{GREEN}{CYAN}========================
{YELLOW}+ -- --=[{RED}Auxiliary{MAGENTA} {auxiliary_count} {RED}{YELLOW}]=-- -- +
{YELLOW}+ -- --=[{RED}Payloads {MAGENTA} {payloads_count}  {RED}{YELLOW}]=-- -- +
{YELLOW}+ -- --=[{RED}Exploits {MAGENTA} {exploits_count}  {RED}{YELLOW}]=-- -- +
{YELLOW}+ -- --=[{RED}Encoders {MAGENTA} {encoders_count}  {RED}{YELLOW}]=-- -- +
{YELLOW}+ -- --=[{RED}evasion {MAGENTA} {evasion_count}  {RED}{YELLOW}]=-- -- +
{YELLOW}+ -- --=[{RED}Post     {MAGENTA} {post_count}      {RED}{YELLOW}]=-- -- +
{YELLOW}+ -- --=[{RED}Nops     {MAGENTA} {nops_count}      {RED}{YELLOW}]=-- -- +
{CYAN}==================={GREEN}[ thgconsole-config ]{GREEN}{CYAN}========================
{YELLOW}+ -- --=[{RED}DB_STATUS =>{MAGENTA}off next fix 2.0.4  {RED}{YELLOW}]=-- -- +
        """.format(os=platform.uname()[0],
                   release=platform.uname()[2],
                   versao=platform.uname()[3],
                   evasion_count=self.modules_count["evasion"],
                   machine=platform.uname()[4],
                   processor=platform.uname()[5],
                   hostname=platform.uname()[1],
                   exploits_count=self.modules_count["exploits"] + self.modules_count['extra_exploits'],
                   encoders_count=self.modules_count["encoders"] + self.modules_count['extra_encoders'],
                   auxiliary_count=self.modules_count["auxiliary"] + self.modules_count['extra_auxiliary'],
                   nops_count=self.modules_count["nops"] + self.modules_count['extra_nops'],
                   payloads_count=self.modules_count["payloads"] + self.modules_count['extra_payloads'],
                   post_count=self.modules_count["post"] + self.modules_count['extra_post'],
                   codenome=__codenome__,
                   version=__version__,
                   CYAN=Fore.CYAN,
                   GREEN=Fore.GREEN,
                   RED=Fore.RED,
                   YELLOW=Fore.YELLOW,
                   MAGENTA=Fore.MAGENTA,
                   gccv=thg_add_init.check_gcc_version(),
                   python=thg_add_init.check_python_version(),
                   net=thg_add_init.is_connected(),
                   ip=thg_add_init.ipi(),
                   mac=thg_add_init.get_mac())
    def ipi(self, darkcde):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        a = s.getsockname()[0]
        return a
    def __parse_THGprompt(self):
        raw_THGprompt_default_template = "\001\033[4m\002{host}\001\033[0m\002 > "
        raw_THGprompt_template = os.getenv("THG_RAW_PROMPT", raw_THGprompt_default_template).replace('\\033', '\033')
        self.raw_THGprompt_template = raw_THGprompt_template if '{host}' in raw_THGprompt_template else raw_THGprompt_default_template

        module_THGprompt_default_template = "\001\033[4m\002{host}\001\033[0m\002 (\001\033[91m\002{module}\001\033[0m\002) > "
        module_THGprompt_template = os.getenv("THG_MODULE_PROMPT", module_THGprompt_default_template).replace('\\033', '\033')
        self.module_THGprompt_template = module_THGprompt_template if all(
            map(lambda x: x in module_THGprompt_template, ['{host}', "{module}"])) else module_THGprompt_default_template
    def __handle_if_noninteractive(self, argv):
        noninteractive = False
        module = ""
        set_opts = []

        try:
            opts, args = getopt.getopt(argv, "hxm:s:", ["module=", "set="])
        except getopt.GetoptError:
            print_info("{} -m <module> -s \"<option> <value>\"".format(sys.argv[0]))
            sys.exit(2)

        for opt, arg in opts:
            if opt == "-h":
                print_info("{} -x -m <module> -s \"<option> <value>\"".format(sys.argv[0]))
                sys.exit(0)
            elif opt == "-x":
                noninteractive = True
            elif opt in ("-m", "--module"):
                module = arg
            elif opt in ("-s", "--set"):
                set_opts.append(arg)

        if noninteractive:
            self.thg_command_use(module)

            for opt in set_opts:
                self.thg_command_set(opt)

            self.thg_command_exploit()

            sys.exit(0)
    @property
    def module_metadata(self):
        return getattr(self.current_module, "_{}__info__".format(self.current_module.__class__.__name__))
    @property
    def THGprompt(self):
        """ Returns THGprompt string based on current_module attribute.

        Adding module prefix (module.name) if current_module attribute is set.

        :return: THGprompt string with appropriate module prefix.
        """
        if self.current_module:
            try:
                return self.module_THGprompt_template.format(host=self.THGprompt_hostname,
                                                          module=self.module_metadata['name'])
            except (AttributeError, KeyError):
                return self.module_THGprompt_template.format(host=self.THGprompt_hostname, module="UnnamedModule")
        else:
            return self.raw_THGprompt_template.format(host=self.THGprompt_hostname)
    def import_extra_package(self):
        if self.extra_package_path:
            extra_modules_dir = os.path.join(self.extra_package_path, "thg_extra_modules")
            if os.path.isdir(extra_modules_dir):
                self.extra_modules_dir = extra_modules_dir
                self.extra_modules_dirs = [module for module in os.listdir(self.extra_modules_dir) if
                                           not module.startswith("__")]
                self.extra_modules = index_extra_modules(modules_directory=self.extra_modules_dir)
                print("extra_modules_dir:%s" % self.extra_modules_dir)
                sys.path.append(self.extra_package_path)
                sys.path.append(self.extra_modules_dir)
        else:
            return
    def available_modules_completion(self, text):
        """ Looking for tab completion hints using setup.py entry_points.

        May need optimization in the future!

        :param text: argument of 'use' thg_command
        :return: list of tab completion hints
        """
        text = pythonize_path(text)
        all_possible_matches = filter(lambda x: x.startswith(text), self.modules)
        matches = set()
        for match in all_possible_matches:
            head, sep, tail = match[len(text):].partition('.')
            if not tail:
                sep = ""
            matches.add("".join((text, head, sep)))
        return list(map(humanize_path, matches))  # humanize output, replace dots to forward slashes
    def suggested_thg_commands(self):
        """ Entry point for intelligent tab completion.

        Based on state of interpreter this method will return intelligent suggestions.

        :return: list of most accurate thg_command suggestions
        """
        if self.current_module and GLOBAL_OPTS:
            return sorted(itertools.chain(self.module_thg_commands, ("unsetg ",)))
        elif self.current_module:
            return self.module_thg_commands
        else:
            return self.global_thg_commands
    ####################################################################################
    ####################################################################################
    ##                            command_console                                     ##
    ####################################################################################
    ####################################################################################
    def thg_command_back(self, *args, **kwargs):
        self.current_module = None
    def thg_command_use(self, module_path, *args, **kwargs):
        if module_path.startswith("extra_"):
            module_path = pythonize_path(module_path)
        else:
            module_path = pythonize_path(module_path)
            module_path = ".".join(("thgconsole", "modules", module_path))
        # module_path, _, exploit_name = module_path.rpartition('.')
        try:
            self.current_module = import_exploit(module_path)()
        except THGtException as err:
            print_error(str(err))
    @stop_after(2)
    def complete_use(self, text, *args, **kwargs):
        if text:
            return self.available_modules_completion(text)
        else:
            if self.extra_modules_dirs:
                return self.main_modules_dirs + self.extra_modules_dirs
            else:
                return self.main_modules_dirs
    @module_required
    def thg_command_edit(self, *args, **kwargs):
        os.system("nano thgconsole/modules/"+str(self.current_module)+".py")
    @module_required
    def thg_command_run(self, *args, **kwargs):
        print_status("Running module...")
        try:
            self.current_module.run()
        except KeyboardInterrupt:
            print_info()
            print_error("Operation cancelled by user")
        except Exception:
            print_error(traceback.format_exc(sys.exc_info()))
    def thg_command_exploit(self, *args, **kwargs):
        self.thg_command_run()
    @module_required
    def thg_command_set(self, *args, **kwargs):
        key, _, value = args[0].partition(" ")
        if key in self.current_module.options:
            setattr(self.current_module, key, value)
            self.current_module.exploit_attributes[key][0] = value

            if kwargs.get("glob", False):
                GLOBAL_OPTS[key] = value
            print_success("{} => {}".format(key, value))
        else:
            print_error("You can't set option '{}'.\n"
                        "Available options: {}".format(key, self.current_module.options))
    @stop_after(2)
    def complete_set(self, text, *args, **kwargs):
        if text:
            return [" ".join((attr, "")) for attr in self.current_module.options if attr.startswith(text)]
        else:
            return self.current_module.options
    @module_required
    def thg_command_setg(self, *args, **kwargs):
        kwargs['glob'] = True
        self.thg_command_set(*args, **kwargs)
    @stop_after(2)
    def complete_setg(self, text, *args, **kwargs):
        return self.complete_set(text, *args, **kwargs)
    @module_required
    def thg_command_unsetg(self, *args, **kwargs):
        key, _, value = args[0].partition(' ')
        try:
            del GLOBAL_OPTS[key]
        except KeyError:
            print_error("You can't unset global option '{}'.\n"
                        "Available global options: {}".format(key, list(GLOBAL_OPTS.keys())))
        else:
            print_success({key: value})
    @stop_after(2)
    def complete_unsetg(self, text, *args, **kwargs):
        if text:
            return [' '.join((attr, "")) for attr in GLOBAL_OPTS.keys() if attr.startswith(text)]
        else:
            return list(GLOBAL_OPTS.keys())
    @module_required
    def get_opts(self, *args):
        """ Generator returning module's Option attributes (option_name, option_value, option_description)

        :param args: Option names
        :return:
        """
        for opt_key in args:
            try:
                opt_description = self.current_module.exploit_attributes[opt_key][1]
                opt_display_value = self.current_module.exploit_attributes[opt_key][0]
            except (KeyError, AttributeError):
                pass
            else:
                yield opt_key, opt_display_value, opt_description
    @stop_after(2)
    def complete_show(self, text, *args, **kwargs):
        if text:
            return [thg_command for thg_command in self.show_sub_thg_commands if thg_command.startswith(text)]
        else:
            return self.show_sub_thg_commands
####################################################################################
####################################################################################
##                            command_help                                        ##
####################################################################################
####################################################################################
    def thg_command_show(self, *args, **kwargs):
        sub_thg_command = args[0]
        try:
            getattr(self, "_show_{}".format(sub_thg_command))(*args, **kwargs)
        except AttributeError:
            print_error("Unknown 'show' sub-thg_command '{}'. "
                        "What do you want to show?\n"
                        "Possible choices are: {}".format(sub_thg_command, self.show_sub_thg_commands))
    @module_required
    def _show_info(self, *args, **kwargs):
        pprint_dict_in_order(
            self.module_metadata,
            ("name", "description", "devices", "authors", "references"),
        )
        print_info()
    @module_required
    def _show_options(self, *args, **kwargs):
        target_names = ["target", "port", "ssl", "rhost", "rport", "lhost", "lport"]
        target_opts = [opt for opt in self.current_module.options if opt in target_names]
        module_opts = [opt for opt in self.current_module.options if opt not in target_opts]
        headers = ("Name", "Current settings", "Description")

        print_info("\nTarget options:")
        print_table(headers, *self.get_opts(*target_opts))

        if module_opts:
            print_info("\nModule options:")
            print_table(headers, *self.get_opts(*module_opts))

        print_info()
    @module_required
    def _show_devices(self, *args, **kwargs):  # TODO: cover with tests
        try:
            devices = self.current_module._Exploit__info__['devices']

            print_info("\nTarget devices:")
            i = 0
            for device in devices:
                if isinstance(device, dict):
                    print_info("   {} - {}".format(i, device['name']))
                else:
                    print_info("   {} - {}".format(i, device))
                i += 1
            print_info()
        except KeyError:
            print_info("\nTarget devices are not defined")
    @module_required
    def _show_wordlists(self, *args, **kwargs):
        headers = ("Wordlist", "Path")
        wordlists = [(f, "file://{}/{}".format(WORDLISTS_DIR, f)) for f in os.listdir(WORDLISTS_DIR) if
                     f.endswith(".txt")]
        listw = str(len(wordlists))
        print_table(headers, *wordlists, max_column_length=9000)
    @module_required
    def _show_encoders(self, *args, **kwargs):
        if issubclass(self.current_module.__class__, BasePayload):
            encoders = self.current_module.get_encoders()
            if encoders:
                headers = ("Encoder", "Name", "Description")
                print_table(headers, *encoders, max_column_length=9000)
                return

        print_error("No encoders available")
    def __show_modules(self, root=''):
        for module in [module for module in self.modules if module.startswith(root)]:
            print_info(module.replace('.', os.sep))
    def _show_all(self, *args, **kwargs):
        self.__show_modules()
    def _show_auxiliary(self,*args,**kwargs):
        self.__show_modules("auxiliary")
    def _show_evasion(self,*args,**kwargs):
        self.__show_modules("evasion")
    def _show_encoders(self, *args, **kwargs):
        self.__show_modules("encoders")
    def _show_exploits(self, *args, **kwargs):
        self.__show_modules('exploits')
    def _show_nops(self, *args, **kwargs):
        self.__show_modules('nops')
    def _show_payloads(self, *args, **kwargs):
        self.__show_modules('payloads')
    def _show_post(self, *args, **kwargs):
        self.__show_modules('post')
    def _show_banner(self, *args, **kwargs):
        os.system("clear")
        print(self.banner)
    def _show_version(self, *args, **kwargs):
        print_status(__codenome__ + "-" + __version__)
    def _show_ip(self, *args, **kwargs):
        print(self.ipi(darkcde=None))
    def _show_history(self, *args, **kwargs):
        os.system("cat ~/.THG_history")
####################################################################################
####################################################################################
##                            command_s                                           ##
####################################################################################
####################################################################################
    @module_required
    def thg_command_check(self, *args, **kwargs):
        try:
            result = self.current_module.check()
        except Exception as error:
            print_error(error)
        else:
            if result is True:
                print_success("Target is vulnerable")
            elif result is False:
                print_error("Target is not vulnerable")
            else:
                print_status("Target could not be verified")
    def thg_command_sleep(self, args, **kwargs):
        print_success("sleep " + str(args))
        sleep(float(args))
    def thg_command_help(self, *args, **kwargs):
        print_info(self.global_help)
        if self.current_module:
            print_info("\n", self.module_help)
    def thg_command_log(self, *args, **kwargs):
        os.system("cat thgconsole.log")
    def thg_command_iptables(self, *args, **kwargs):
        thg_commandos = '''usage: iptables [-h/--help]
        optional arguments:
          -h, --help   show help
        '''  # aqui fica os comentarios do seus argumentos
        short_cm = ''''''
        if args == "":
            print(short_cm)
    def thg_command_del(self,args,**kwargs):
        thg_commandos = '''usage: dell [-h/--help] [--list] [file]
optional arguments:
  -h, --help   show help
  --list       list files 
''' # aqui fica os comentarios do seus argumentos
        short_cm = '''[--list] list files \n[--help] show all info'''
        if args == "":
            print(short_cm)
        elif args == "-h":
            print(thg_commandos)
        elif args == "--help":
            print(thg_commandos)
        if os.path.isdir(args) == True:
            print_success("del dir...[%s]".format(args))
            shutil.rmtree(args)
            print_success("dir deleted successfully => "+(args))
        elif args == "list":
            dir = os.getcwd()
            directories = [d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]
            file = [d for d in os.listdir(os.getcwd()) if os.path.isfile(d)]
            print_status("dir:: " + dir)
            print_status(" FILE:" + str(len(file)) + " FOLDER:" + str(len(directories)))
            arquivos = []
            pastas = []
            for i in glob("*"):
                if os.path.isdir(i) == True:
                    print(Fore.CYAN + i + Fore.LIGHTYELLOW_EX + "/")

                else:
                    print(Fore.RED + i)

        elif os.path.isfile(args) == True:
            print_success("del file...[{}]".format(args))
            os.remove(args)
            print_success("file deleted successfully => "+args)
        elif os.path.islink(args)==True:
            print_success("del link..[{}]".format(args))
            import pathlib
            pathlib.Path.unlink(args)
            print_success("link deleted successfully => "+args)
            del pathlib
    def thg_command_exec(self, *args, **kwargs):
        os.system(args[0])
    def thg_command_shell(self, *args, **kwargs):
        os.system("bash")
    def thg_command_color(self, args, **kwargs):
        self.THGprompt_hostname = args
    def thg_command_python_interpreter(self, *args, **kwargs):
        os.system("python3")
    def thg_command_route(self, args, **kwargs):
        os.system("route " + args)
    def thg_command_cd(self, *args, **kwargs):
        dir = os.getcwd()
        try:
            heck = os.path.exists(args[0])

            total = glob(args[0] + "/*")
            print_status("current: " + dir)
            if args[0] == "":
                pass
            else:
                changer_dir = os.chdir(args[0])
                dir = os.getcwd()
                directories = [d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]
                file = [d for d in os.listdir(os.getcwd()) if os.path.isfile(d)]
                print_status("change: " + dir)
                print_status("total:" + str(len(total)) + " FILE:" + str(len(file)) + " FOLDER:" + str(len(directories)))
                arquivos = []
                pastas = []
                for i in glob("*"):
                    if os.path.isdir(i) == True:
                        print(Fore.CYAN + i + Fore.LIGHTYELLOW_EX + "/")

                    else:
                        print(Fore.RED + i)
        except:
            pass
    def thg_command_quit(self, *args, **kwargs):
        print_status("thgconsole stopped")
        exit(1)
    def thg_command_search(self, *args, **kwargs):
        keyword = args[0]

        if not keyword:
            print_error("Please specify search keyword. e.g. 'search cisco'")
            return

        for module in self.modules:
            if keyword in module:
                module = humanize_path(module)
                print_info(
                    "{}\033[31m{}\033[0m{}".format(*module.partition(keyword))
                )
    def thg_command_exit(self, *args, **kwargs):
        raise EOFError
####################################################################################
####################################################################################
##                            command_systemADM                                   ##
####################################################################################
####################################################################################
    def thg_command_battery(self, *args, **kwargs):

        def secs2hours(secs):
            mm, ss = divmod(secs, 60)
            hh, mm = divmod(mm, 60)
            return "%d:%02d:%02d" % (hh, mm, ss)

        def main():
            if not hasattr(psutil, "sensors_battery"):
                return sys.exit("platform not supported")
            batt = psutil.sensors_battery()
            if batt is None:
                return sys.exit("no battery is installed")

            print("charge:     %s%%" % round(batt.percent, 2))
            if batt.power_plugged:
                print("status:     %s" % (
                    "charging" if batt.percent < 100 else "fully charged"))
                print("plugged in: yes")
            else:
                print("left:       %s" % secs2hours(batt.secsleft))
                print("status:     %s" % "discharging")
                print("plugged in: no")

        main()
    def thg_command_disk_usage(self, *args, **kwargs):

        templ = "%-17s %8s %8s %8s %5s%% %9s  %s"
        print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type",
                       "Mount"))
        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':
                if 'cdrom' in part.opts or part.fstype == '':
                    # skip cd-rom drives with no disk in it; they may raise
                    # ENOENT, pop-up a Windows GUI error for a non-ready
                    # partition or just hang.
                    continue
            usage = psutil.disk_usage(part.mountpoint)
            print(templ % (
                part.device,
                bytes2human(usage.total),
                bytes2human(usage.used),
                bytes2human(usage.free),
                int(usage.percent),
                part.fstype,
                part.mountpoint))
    def thg_command_meminfo(self, *args, **kwargs):
        def pprint_ntuple(nt):
            for name in nt._fields:
                value = getattr(nt, name)
                if name != 'percent':
                    value = bytes2human(value)
                print('%-10s : %7s' % (name.capitalize(), value))
        def main():
            print('MEMORY\n------')
            pprint_ntuple(psutil.virtual_memory())
            print('\nSWAP\n----')
            pprint_ntuple(psutil.swap_memory())

        main()
    def thg_command_fans(self, *args, **kwargs):
        if not hasattr(psutil, "sensors_fans"):
            return sys.exit("platform not supported")
        fans = psutil.sensors_fans()
        if not fans:
            print("no fans detected")
            return
        for name, entries in fans.items():
            print(name)
        for entry in entries:
            print("    %-20s %s RPM" % (entry.label or name, entry.current))
    def thg_command_free(self, *args, **kwargs):
        def main():
            virt = psutil.virtual_memory()
            swap = psutil.swap_memory()
            templ = "%-7s %10s %10s %10s %10s %10s %10s"
            print(templ % ('', 'total', 'used', 'free', 'shared', 'buffers', 'cache'))
            print(templ % (
                'Mem:',
                int(virt.total / 1024),
                int(virt.used / 1024),
                int(virt.free / 1024),
                int(getattr(virt, 'shared', 0) / 1024),
                int(getattr(virt, 'buffers', 0) / 1024),
                int(getattr(virt, 'cached', 0) / 1024)))
            print(templ % (
                'Swap:', int(swap.total / 1024),
                int(swap.used / 1024),
                int(swap.free / 1024),
                '',
                '',
                ''))

        main()
    def thg_command_ifconfig(self, *args, **kwargs):
        af_map = {
            socket.AF_INET: 'IPv4',
            socket.AF_INET6: 'IPv6',
            psutil.AF_LINK: 'MAC',
        }

        duplex_map = {
            psutil.NIC_DUPLEX_FULL: "full",
            psutil.NIC_DUPLEX_HALF: "half",
            psutil.NIC_DUPLEX_UNKNOWN: "?",
        }

        def main():
            stats = psutil.net_if_stats()
            io_counters = psutil.net_io_counters(pernic=True)
            for nic, addrs in psutil.net_if_addrs().items():
                print("%s:" % (nic))
                if nic in stats:
                    st = stats[nic]
                    print("    stats          : ", end='')
                    print("speed=%sMB, duplex=%s, mtu=%s, up=%s" % (
                        st.speed, duplex_map[st.duplex], st.mtu,
                        "yes" if st.isup else "no"))
                if nic in io_counters:
                    io = io_counters[nic]
                    print("    incoming       : ", end='')
                    print("bytes=%s, pkts=%s, errs=%s, drops=%s" % (
                        bytes2human(io.bytes_recv), io.packets_recv, io.errin,
                        io.dropin))
                    print("    outgoing       : ", end='')
                    print("bytes=%s, pkts=%s, errs=%s, drops=%s" % (
                        bytes2human(io.bytes_sent), io.packets_sent, io.errout,
                        io.dropout))
                for addr in addrs:
                    print("    %-4s" % af_map.get(addr.family, addr.family), end="")
                    print(" address   : %s" % addr.address)
                    if addr.broadcast:
                        print("         broadcast : %s" % addr.broadcast)
                    if addr.netmask:
                        print("         netmask   : %s" % addr.netmask)
                    if addr.ptp:
                        print("      p2p       : %s" % addr.ptp)
                print("")


        main()
    def thg_command_netstat(self, *args, **kwargs):
        # !/usr/bin/env python

        # Copyright (c) 2009, Giampaolo Rodola'. All rights reserved.
        # Use of this source code is governed by a BSD-style license that can be
        # found in the LICENSE file.

        """
        A clone of 'netstat -antp' on Linux.

        $ python scripts/netstat.py
        Proto Local address      Remote address   Status        PID    Program name
        tcp   127.0.0.1:48256    127.0.0.1:45884  ESTABLISHED   13646  chrome
        tcp   127.0.0.1:47073    127.0.0.1:45884  ESTABLISHED   13646  chrome
        tcp   127.0.0.1:47072    127.0.0.1:45884  ESTABLISHED   13646  chrome
        tcp   127.0.0.1:45884    -                LISTEN        13651  GoogleTalkPlugi
        tcp   127.0.0.1:60948    -                LISTEN        13651  GoogleTalkPlugi
        tcp   172.17.42.1:49102  127.0.0.1:19305  CLOSE_WAIT    13651  GoogleTalkPlugi
        tcp   172.17.42.1:55797  127.0.0.1:443    CLOSE_WAIT    13651  GoogleTalkPlugi
        ...
        """

        import socket
        from socket import AF_INET, SOCK_STREAM, SOCK_DGRAM

        import psutil

        AD = "-"
        AF_INET6 = getattr(socket, 'AF_INET6', object())
        proto_map = {
            (AF_INET, SOCK_STREAM): 'tcp',
            (AF_INET6, SOCK_STREAM): 'tcp6',
            (AF_INET, SOCK_DGRAM): 'udp',
            (AF_INET6, SOCK_DGRAM): 'udp6',
        }

        def main():
            templ = "%-5s %-30s %-30s %-13s %-6s %s"
            print(templ % (
                "Proto", "Local address", "Remote address", "Status", "PID",
                "Program name"))
            proc_names = {}
            for p in psutil.process_iter(attrs=['pid', 'name']):
                proc_names[p.info['pid']] = p.info['name']
            for c in psutil.net_connections(kind='inet'):
                laddr = "%s:%s" % (c.laddr)
                raddr = ""
                if c.raddr:
                    raddr = "%s:%s" % (c.raddr)
                print(templ % (
                    proto_map[(c.family, c.type)],
                    laddr,
                    raddr or AD,
                    c.status,
                    c.pid or AD,
                    proc_names.get(c.pid, '?')[:15],
                ))

        main()



        import atexit
        import time
        import sys
        try:
            import curses
        except ImportError:
            sys.exit('platform not supported')

        import psutil
        from psutil._common import bytes2human

        def tear_down():
            win.keypad(0)
            curses.nocbreak()
            curses.echo()
            curses.endwin()

        win = curses.initscr()
        atexit.register(tear_down)
        curses.endwin()
        lineno = 0

        def print_line(line, highlight=False):
            """A thin wrapper around curses's addstr()."""
            global lineno
            try:
                if highlight:
                    line += " " * (win.getmaxyx()[1] - len(line))
                    win.addstr(lineno, 0, line, curses.A_REVERSE)
                else:
                    win.addstr(lineno, 0, line, 0)
            except curses.error:
                lineno = 0
                win.refresh()
                raise
            else:
                lineno += 1

        def poll(interval):
            """Retrieve raw stats within an interval window."""
            tot_before = psutil.net_io_counters()
            pnic_before = psutil.net_io_counters(pernic=True)
            # sleep some time
            time.sleep(interval)
            tot_after = psutil.net_io_counters()
            pnic_after = psutil.net_io_counters(pernic=True)
            return (tot_before, tot_after, pnic_before, pnic_after)

        def refresh_window(tot_before, tot_after, pnic_before, pnic_after):
            """Print stats on screen."""
            global lineno

            # totals
            print_line("total bytes:           sent: %-10s   received: %s" % (
                bytes2human(tot_after.bytes_sent),
                bytes2human(tot_after.bytes_recv))
                       )
            print_line("total packets:         sent: %-10s   received: %s" % (
                tot_after.packets_sent, tot_after.packets_recv))

            # per-network interface details: let's sort network interfaces so
            # that the ones which generated more traffic are shown first
            print_line("")
            nic_names = list(pnic_after.keys())
            nic_names.sort(key=lambda x: sum(pnic_after[x]), reverse=True)
            for name in nic_names:
                stats_before = pnic_before[name]
                stats_after = pnic_after[name]
                templ = "%-15s %15s %15s"
                print_line(templ % (name, "TOTAL", "PER-SEC"), highlight=True)
                print_line(templ % (
                    "bytes-sent",
                    bytes2human(stats_after.bytes_sent),
                    bytes2human(
                        stats_after.bytes_sent - stats_before.bytes_sent) + '/s',
                ))
                print_line(templ % (
                    "bytes-recv",
                    bytes2human(stats_after.bytes_recv),
                    bytes2human(
                        stats_after.bytes_recv - stats_before.bytes_recv) + '/s',
                ))
                print_line(templ % (
                    "pkts-sent",
                    stats_after.packets_sent,
                    stats_after.packets_sent - stats_before.packets_sent,
                ))
                print_line(templ % (
                    "pkts-recv",
                    stats_after.packets_recv,
                    stats_after.packets_recv - stats_before.packets_recv,
                ))
                print_line("")
            win.refresh()
            lineno = 0

        def main():
            try:
                interval = 0
                while True:
                    args = poll(interval)
                    refresh_window(*args)
                    interval = 1
            except (KeyboardInterrupt, SystemExit):
                pass

        if __name__ == '__main__':
            main()
    def thg_command_nettop(self, *args, **kwargs):
        import atexit
        import time
        import sys
        try:
            import curses
        except ImportError:
            sys.exit('platform not supported')

        import psutil
        from psutil._common import bytes2human

        def tear_down():
            win.keypad(0)
            curses.nocbreak()
            curses.echo()
            curses.endwin()

        win = curses.initscr()
        atexit.register(tear_down)
        curses.endwin()
        lineno = 0

        def print_line(line, highlight=False):
            """A thin wrapper around curses's addstr()."""
            global lineno
            try:
                if highlight:
                    line += " " * (win.getmaxyx()[1] - len(line))
                    win.addstr(lineno, 0, line, curses.A_REVERSE)
                else:
                    win.addstr(lineno, 0, line, 0)
            except curses.error:
                lineno = 0
                win.refresh()
                raise
            else:
                lineno += 1

        def poll(interval):
            """Retrieve raw stats within an interval window."""
            tot_before = psutil.net_io_counters()
            pnic_before = psutil.net_io_counters(pernic=True)
            # sleep some time
            time.sleep(interval)
            tot_after = psutil.net_io_counters()
            pnic_after = psutil.net_io_counters(pernic=True)
            return (tot_before, tot_after, pnic_before, pnic_after)

        def refresh_window(tot_before, tot_after, pnic_before, pnic_after):
            """Print stats on screen."""
            global lineno

            # totals
            print_line("total bytes:           sent: %-10s   received: %s" % (
                bytes2human(tot_after.bytes_sent),
                bytes2human(tot_after.bytes_recv))
                       )
            print_line("total packets:         sent: %-10s   received: %s" % (
                tot_after.packets_sent, tot_after.packets_recv))

            # per-network interface details: let's sort network interfaces so
            # that the ones which generated more traffic are shown first
            print_line("")
            nic_names = list(pnic_after.keys())
            nic_names.sort(key=lambda x: sum(pnic_after[x]), reverse=True)
            for name in nic_names:
                stats_before = pnic_before[name]
                stats_after = pnic_after[name]
                templ = "%-15s %15s %15s"
                print_line(templ % (name, "TOTAL", "PER-SEC"), highlight=True)
                print_line(templ % (
                    "bytes-sent",
                    bytes2human(stats_after.bytes_sent),
                    bytes2human(
                        stats_after.bytes_sent - stats_before.bytes_sent) + '/s',
                ))
                print_line(templ % (
                    "bytes-recv",
                    bytes2human(stats_after.bytes_recv),
                    bytes2human(
                        stats_after.bytes_recv - stats_before.bytes_recv) + '/s',
                ))
                print_line(templ % (
                    "pkts-sent",
                    stats_after.packets_sent,
                    stats_after.packets_sent - stats_before.packets_sent,
                ))
                print_line(templ % (
                    "pkts-recv",
                    stats_after.packets_recv,
                    stats_after.packets_recv - stats_before.packets_recv,
                ))
                print_line("")
            win.refresh()
            lineno = 0

        def main():
            try:
                interval = 0
                while True:
                    args = poll(interval)
                    refresh_window(*args)
                    interval = 1
            except (KeyboardInterrupt, SystemExit):
                pass

        main()

    def thg_command_pmap(self, *args, **kwargs):
        # !/usr/bin/env python

        # Copyright (c) 2009, Giampaolo Rodola'. All rights reserved.
        # Use of this source code is governed by a BSD-style license that can be
        # found in the LICENSE file.

        """
        A clone of 'pmap' utility on Linux, 'vmmap' on macOS and 'procstat -v' on BSD.
        Report memory map of a process.

        $ python scripts/pmap.py 32402
        Address                 RSS  Mode    Mapping
        0000000000400000      1200K  r-xp    /usr/bin/python2.7
        0000000000838000         4K  r--p    /usr/bin/python2.7
        0000000000839000       304K  rw-p    /usr/bin/python2.7
        00000000008ae000        68K  rw-p    [anon]
        000000000275e000      5396K  rw-p    [heap]
        00002b29bb1e0000       124K  r-xp    /lib/x86_64-linux-gnu/ld-2.17.so
        00002b29bb203000         8K  rw-p    [anon]
        00002b29bb220000       528K  rw-p    [anon]
        00002b29bb2d8000       768K  rw-p    [anon]
        00002b29bb402000         4K  r--p    /lib/x86_64-linux-gnu/ld-2.17.so
        00002b29bb403000         8K  rw-p    /lib/x86_64-linux-gnu/ld-2.17.so
        00002b29bb405000        60K  r-xp    /lib/x86_64-linux-gnu/libpthread-2.17.so
        00002b29bb41d000         0K  ---p    /lib/x86_64-linux-gnu/libpthread-2.17.so
        00007fff94be6000        48K  rw-p    [stack]
        00007fff94dd1000         4K  r-xp    [vdso]
        ffffffffff600000         0K  r-xp    [vsyscall]
        ...
        """
        from psutil._compat import get_terminal_size

        def safe_print(s):
            s = s[:get_terminal_size()[0]]
            try:
                print(s)
            except UnicodeEncodeError:
                print(s.encode('ascii', 'ignore').decode())

        def main():
            p = psutil.Process(int(args[0]))
            templ = "%-20s %10s  %-7s %s"
            print(templ % ("Address", "RSS", "Mode", "Mapping"))
            total_rss = 0
            for m in p.memory_maps(grouped=False):
                total_rss += m.rss
                safe_print(templ % (
                    m.addr.split('-')[0].zfill(16),
                    bytes2human(m.rss),
                    m.perms,
                    m.path))
            print("-" * 31)
            print(templ % ("Total", bytes2human(total_rss), '', ''))
            safe_print("PID = %s, name = %s" % (p.pid, p.name()))

        main()
    def thg_command_who(self, *args, **kwargs):
        # !/usr/bin/env python

        # Copyright (c) 2009, Giampaolo Rodola'. All rights reserved.
        # Use of this source code is governed by a BSD-style license that can be
        # found in the LICENSE file.

        """
        A clone of 'who' command; print information about users who are
        currently logged in.

        $ python scripts/who.py
        giampaolo    console    2017-03-25 22:24                loginwindow
        giampaolo    ttys000    2017-03-25 23:28 (10.0.2.2)     sshd
        """

        from datetime import datetime

        import psutil

        def main():
            users = psutil.users()
            for user in users:
                proc_name = psutil.Process(user.pid).name() if user.pid else ""
                print("%-12s %-10s %-10s %-14s %s" % (
                    user.name,
                    user.terminal or '-',
                    datetime.fromtimestamp(user.started).strftime("%Y-%m-%d %H:%M"),
                    "(%s)" % user.host if user.host else "",
                    proc_name
                ))

        main()
    def thg_command_htop(self, *args, **kwargs):
        # !/usr/bin/env python

        # Copyright (c) 2009, Giampaolo Rodola'. All rights reserved.
        # Use of this source code is governed by a BSD-style license that can be
        # found in the LICENSE file.

        """
        A clone of top / htop.

        Author: Giampaolo Rodola' <g.rodola@gmail.com>

        $ python scripts/top.py
         CPU0  [||||                                    ]  10.9%
         CPU1  [|||||                                   ]  13.1%
         CPU2  [|||||                                   ]  12.8%
         CPU3  [||||                                    ]  11.5%
         Mem   [|||||||||||||||||||||||||||||           ]  73.0% 11017M / 15936M
         Swap  [                                        ]   1.3%   276M / 20467M
         Processes: 347 (sleeping=273, running=1, idle=73)
         Load average: 1.10 1.28 1.34  Uptime: 8 days, 21:15:40

        PID    USER       NI   VIRT    RES  CPU%  MEM%     TIME+  NAME
        5368   giampaol    0   7.2G   4.3G  41.8  27.7  56:34.18  VirtualBox
        24976  giampaol    0   2.1G 487.2M  18.7   3.1  22:05.16  Web Content
        22731  giampaol    0   3.2G 596.2M  11.6   3.7  35:04.90  firefox
        1202   root        0 807.4M 288.5M  10.6   1.8  12:22.12  Xorg
        22811  giampaol    0   2.8G 741.8M   9.0   4.7   2:26.61  Web Content
        2590   giampaol    0   2.3G 579.4M   5.5   3.6  28:02.70  compiz
        22990  giampaol    0   3.0G   1.2G   4.2   7.6   4:30.32  Web Content
        18412  giampaol    0  90.1M  14.5M   3.5   0.1   0:00.26  python3
        26971  netdata     0  20.8M   3.9M   2.9   0.0   3:17.14  apps.plugin
        2421   giampaol    0   3.3G  36.9M   2.3   0.2  57:14.21  pulseaudio
        ...
        """

        import atexit
        import datetime
        import sys
        import time
        try:
            import curses
        except ImportError:
            sys.exit('platform not supported')

        import psutil
        from psutil._common import bytes2human

        # --- curses stuff

        def tear_down():
            win.keypad(0)
            curses.nocbreak()
            curses.echo()
            curses.endwin()

        win = curses.initscr()
        atexit.register(tear_down)
        curses.endwin()
        lineno = 0

        def print_line(line, highlight=False):
            """A thin wrapper around curses's addstr()."""
            global lineno
            try:
                if highlight:
                    line += " " * (win.getmaxyx()[1] - len(line))
                    win.addstr(lineno, 0, line, curses.A_REVERSE)
                else:
                    win.addstr(lineno, 0, line, 0)
            except curses.error:
                lineno = 0
                win.refresh()
                raise
            else:
                lineno += 1

        # --- /curses stuff

        def poll(interval):
            # sleep some time
            time.sleep(interval)
            procs = []
            procs_status = {}
            for p in psutil.process_iter():
                try:
                    p.dict = p.as_dict(['username', 'nice', 'memory_info',
                                        'memory_percent', 'cpu_percent',
                                        'cpu_times', 'name', 'status'])
                    try:
                        procs_status[p.dict['status']] += 1
                    except KeyError:
                        procs_status[p.dict['status']] = 1
                except psutil.NoSuchProcess:
                    pass
                else:
                    procs.append(p)

            # return processes sorted by CPU percent usage
            processes = sorted(procs, key=lambda p: p.dict['cpu_percent'],
                               reverse=True)
            return (processes, procs_status)

        def print_header(procs_status, num_procs):
            """Print system-related info, above the process list."""

            def get_dashes(perc):
                dashes = "|" * int((float(perc) / 10 * 4))
                empty_dashes = " " * (40 - len(dashes))
                return dashes, empty_dashes

            # cpu usage
            percs = psutil.cpu_percent(interval=0, percpu=True)
            for cpu_num, perc in enumerate(percs):
                dashes, empty_dashes = get_dashes(perc)
                print_line(" CPU%-2s [%s%s] %5s%%" % (cpu_num, dashes, empty_dashes,
                                                      perc))
            mem = psutil.virtual_memory()
            dashes, empty_dashes = get_dashes(mem.percent)
            line = " Mem   [%s%s] %5s%% %6s / %s" % (
                dashes, empty_dashes,
                mem.percent,
                str(int(mem.used / 1024 / 1024)) + "M",
                str(int(mem.total / 1024 / 1024)) + "M"
            )
            print_line(line)

            # swap usage
            swap = psutil.swap_memory()
            dashes, empty_dashes = get_dashes(swap.percent)
            line = " Swap  [%s%s] %5s%% %6s / %s" % (
                dashes, empty_dashes,
                swap.percent,
                str(int(swap.used / 1024 / 1024)) + "M",
                str(int(swap.total / 1024 / 1024)) + "M"
            )
            print_line(line)

            # processes number and status
            st = []
            for x, y in procs_status.items():
                if y:
                    st.append("%s=%s" % (x, y))
            st.sort(key=lambda x: x[:3] in ('run', 'sle'), reverse=1)
            print_line(" Processes: %s (%s)" % (num_procs, ', '.join(st)))
            # load average, uptime
            uptime = datetime.datetime.now() - \
                     datetime.datetime.fromtimestamp(psutil.boot_time())
            av1, av2, av3 = psutil.getloadavg()
            line = " Load average: %.2f %.2f %.2f  Uptime: %s" \
                   % (av1, av2, av3, str(uptime).split('.')[0])
            print_line(line)

        def refresh_window(procs, procs_status):
            """Print results on screen by using curses."""
            curses.endwin()
            templ = "%-6s %-8s %4s %6s %6s %5s %5s %9s  %2s"
            win.erase()
            header = templ % ("PID", "USER", "NI", "VIRT", "RES", "CPU%", "MEM%",
                              "TIME+", "NAME")
            print_header(procs_status, len(procs))
            print_line("")
            print_line(header, highlight=True)
            for p in procs:
                # TIME+ column shows process CPU cumulative time and it
                # is expressed as: "mm:ss.ms"
                if p.dict['cpu_times'] is not None:
                    ctime = datetime.timedelta(seconds=sum(p.dict['cpu_times']))
                    ctime = "%s:%s.%s" % (ctime.seconds // 60 % 60,
                                          str((ctime.seconds % 60)).zfill(2),
                                          str(ctime.microseconds)[:2])
                else:
                    ctime = ''
                if p.dict['memory_percent'] is not None:
                    p.dict['memory_percent'] = round(p.dict['memory_percent'], 1)
                else:
                    p.dict['memory_percent'] = ''
                if p.dict['cpu_percent'] is None:
                    p.dict['cpu_percent'] = ''
                if p.dict['username']:
                    username = p.dict['username'][:8]
                else:
                    username = ""
                line = templ % (p.pid,
                                username,
                                p.dict['nice'],
                                bytes2human(getattr(p.dict['memory_info'], 'vms', 0)),
                                bytes2human(getattr(p.dict['memory_info'], 'rss', 0)),
                                p.dict['cpu_percent'],
                                p.dict['memory_percent'],
                                ctime,
                                p.dict['name'] or '',
                                )
                try:
                    print_line(line)
                except curses.error:
                    break
                win.refresh()

        def main():
            try:
                interval = 0
                while True:
                    args = poll(interval)
                    refresh_window(*args)
                    interval = 1
            except (KeyboardInterrupt, SystemExit):
                pass


        main()
    def thg_command_temperatures(self, *args, **kwargs):

        def main():
            if not hasattr(psutil, "sensors_temperatures"):
                sys.exit("platform not supported")
            temps = psutil.sensors_temperatures()
            if not temps:
                sys.exit("can't read any temperature")
            for name, entries in temps.items():
                print(name)
                for entry in entries:
                    print("    %-20s %s °C (high = %s °C, critical = %s °C)" % (
                        entry.label or name, entry.current, entry.high,
                        entry.critical))
                print()

        main()
    def thg_command_sensors(self, *args, **kwargs):

        def secs2hours(secs):
            mm, ss = divmod(secs, 60)
            hh, mm = divmod(mm, 60)
            return "%d:%02d:%02d" % (hh, mm, ss)

        def main():
            if hasattr(psutil, "sensors_temperatures"):
                temps = psutil.sensors_temperatures()
            else:
                temps = {}
            if hasattr(psutil, "sensors_fans"):
                fans = psutil.sensors_fans()
            else:
                fans = {}
            if hasattr(psutil, "sensors_battery"):
                battery = psutil.sensors_battery()
            else:
                battery = None

            if not any((temps, fans, battery)):
                print("can't read any temperature, fans or battery info")
                return

            names = set(list(temps.keys()) + list(fans.keys()))
            for name in names:
                print(name)
                # Temperatures.
                if name in temps:
                    print("    Temperatures:")
                    for entry in temps[name]:
                        print("        %-20s %s°C (high=%s°C, critical=%s°C)" % (
                            entry.label or name, entry.current, entry.high,
                            entry.critical))
                # Fans.
                if name in fans:
                    print("    Fans:")
                    for entry in fans[name]:
                        print("        %-20s %s RPM" % (
                            entry.label or name, entry.current))

            # Battery.
            if battery:
                print("Battery:")
                print("    charge:     %s%%" % round(battery.percent, 2))
                if battery.power_plugged:
                    print("    status:     %s" % (
                        "charging" if battery.percent < 100 else "fully charged"))
                    print("    plugged in: yes")
                else:
                    print("    left:       %s" % secs2hours(battery.secsleft))
                    print("    status:     %s" % "discharging")
                    print("    plugged in: no")

        main()
    def thg_command_pstree(self, *args, **kwargs):
        import collections


        def print_tree(parent, tree, indent=''):
            try:
                name = psutil.Process(parent).name()
            except psutil.Error:
                name = "?"
            print(parent, name)
            if parent not in tree:
                return
            children = tree[parent][:-1]
            for child in children:
                sys.stdout.write(indent + "|- ")
                print_tree(child, tree, indent + "| ")
            child = tree[parent][-1]
            sys.stdout.write(indent + "`_ ")
            print_tree(child, tree, indent + "  ")

        def main():
            # construct a dict where 'values' are all the processes
            # having 'key' as their parent
            tree = collections.defaultdict(list)
            for p in psutil.process_iter():
                try:
                    tree[p.ppid()].append(p.pid)
                except (psutil.NoSuchProcess, psutil.ZombieProcess):
                    pass
            # on systems supporting PID 0, PID 0's parent is usually 0
            if 0 in tree and 0 in tree[0]:
                tree[0].remove(0)
            print_tree(min(tree), tree)

        main()
    def thg_command_ps(self, *args, **kwargs):
        import datetime
        import time
        from psutil._compat import get_terminal_size

        def main():
            today_day = datetime.date.today()
            templ = "%-10s %5s %5s %7s %7s %5s %6s %6s %6s  %s"
            attrs = ['pid', 'memory_percent', 'name', 'cmdline', 'cpu_times',
                     'create_time', 'memory_info', 'status', 'nice', 'username']
            print(templ % ("USER", "PID", "%MEM", "VSZ", "RSS", "NICE",
                           "STATUS", "START", "TIME", "CMDLINE"))
            for p in psutil.process_iter(attrs, ad_value=None):
                if p.info['create_time']:
                    ctime = datetime.datetime.fromtimestamp(p.info['create_time'])
                    if ctime.date() == today_day:
                        ctime = ctime.strftime("%H:%M")
                    else:
                        ctime = ctime.strftime("%b%d")
                else:
                    ctime = ''
                if p.info['cpu_times']:
                    cputime = time.strftime("%M:%S",
                                            time.localtime(sum(p.info['cpu_times'])))
                else:
                    cputime = ''

                user = p.info['username']
                if not user and psutil.POSIX:
                    try:
                        user = p.uids()[0]
                    except psutil.Error:
                        pass
                if user and psutil.WINDOWS and '\\' in user:
                    user = user.split('\\')[1]
                user = user[:9]
                vms = bytes2human(p.info['memory_info'].vms) if \
                    p.info['memory_info'] is not None else ''
                rss = bytes2human(p.info['memory_info'].rss) if \
                    p.info['memory_info'] is not None else ''
                memp = round(p.info['memory_percent'], 1) if \
                    p.info['memory_percent'] is not None else ''
                nice = int(p.info['nice']) if p.info['nice'] else ''
                if p.info['cmdline']:
                    cmdline = ' '.join(p.info['cmdline'])
                else:
                    cmdline = p.info['name']
                status = p.info['status'][:5] if p.info['status'] else ''

                line = templ % (
                    user[:10],
                    p.info['pid'],
                    memp,
                    vms,
                    rss,
                    nice,
                    status,
                    ctime,
                    cputime,
                    cmdline)
                print(line[:get_terminal_size()[0]])

        main()
    def thg_command_procsmem(self, *args, **kwargs):
        import psutil
        if not (psutil.LINUX or psutil.MACOS or psutil.WINDOWS):
            sys.exit("platform not supported")
        def convert_bytes(n):
            symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
            prefix = {}
            for i, s in enumerate(symbols):
                prefix[s] = 1 << (i + 1) * 10
            for s in reversed(symbols):
                if n >= prefix[s]:
                    value = float(n) / prefix[s]
                    return '%.1f%s' % (value, s)
            return "%sB" % n

        def main():
            ad_pids = []
            procs = []
            for p in psutil.process_iter():
                with p.oneshot():
                    try:
                        mem = p.memory_full_info()
                        info = p.as_dict(attrs=["cmdline", "username"])
                    except psutil.AccessDenied:
                        ad_pids.append(p.pid)
                    except psutil.NoSuchProcess:
                        pass
                    else:
                        p._uss = mem.uss
                        p._rss = mem.rss
                        if not p._uss:
                            continue
                        p._pss = getattr(mem, "pss", "")
                        p._swap = getattr(mem, "swap", "")
                        p._info = info
                        procs.append(p)

            procs.sort(key=lambda p: p._uss)
            templ = "%-7s %-7s %-30s %7s %7s %7s %7s"
            print(templ % ("PID", "User", "Cmdline", "USS", "PSS", "Swap", "RSS"))
            print("=" * 78)
            for p in procs[:86]:
                line = templ % (
                    p.pid,
                    p._info["username"][:7] if p._info["username"] else "",
                    " ".join(p._info["cmdline"])[:30],
                    convert_bytes(p._uss),
                    convert_bytes(p._pss) if p._pss != "" else "",
                    convert_bytes(p._swap) if p._swap != "" else "",
                    convert_bytes(p._rss),
                )
                print(line)
            if ad_pids:
                print("warning: access denied for %s pids" % (len(ad_pids)),
                      file=sys.stderr)

        sys.exit(main())
    def thg_command_procinfo(self, *args, **kwargs):
        # !/usr/bin/env python

        # Copyright (c) 2009, Giampaolo Rodola'. All rights reserved.
        # Use of this source code is governed by a BSD-style license that can be
        # found in the LICENSE file.

        """
        Print detailed information about a process.
        Author: Giampaolo Rodola' <g.rodola@gmail.com>

        $ python scripts/procinfo.py
        pid           4600
        name          chrome
        parent        4554 (bash)
        exe           /opt/google/chrome/chrome
        cwd           /home/giampaolo
        cmdline       /opt/google/chrome/chrome
        started       2016-09-19 11:12
        cpu-tspent    27:27.68
        cpu-times     user=8914.32, system=3530.59,
                      children_user=1.46, children_system=1.31
        cpu-affinity  [0, 1, 2, 3, 4, 5, 6, 7]
        memory        rss=520.5M, vms=1.9G, shared=132.6M, text=95.0M, lib=0B,
                      data=816.5M, dirty=0B
        memory %      3.26
        user          giampaolo
        uids          real=1000, effective=1000, saved=1000
        uids          real=1000, effective=1000, saved=1000
        terminal      /dev/pts/2
        status        sleeping
        nice          0
        ionice        class=IOPriority.IOPRIO_CLASS_NONE, value=0
        num-threads   47
        num-fds       379
        I/O           read_count=96.6M, write_count=80.7M,
                      read_bytes=293.2M, write_bytes=24.5G
        ctx-switches  voluntary=30426463, involuntary=460108
        children      PID    NAME
                      4605   cat
                      4606   cat
                      4609   chrome
                      4669   chrome
        open-files    PATH
                      /opt/google/chrome/icudtl.dat
                      /opt/google/chrome/snapshot_blob.bin
                      /opt/google/chrome/natives_blob.bin
                      /opt/google/chrome/chrome_100_percent.pak
                      [...]
        connections   PROTO LOCAL ADDR            REMOTE ADDR               STATUS
                      UDP   10.0.0.3:3693         *:*                       NONE
                      TCP   10.0.0.3:55102        172.217.22.14:443         ESTABLISHED
                      UDP   10.0.0.3:35172        *:*                       NONE
                      TCP   10.0.0.3:32922        172.217.16.163:443        ESTABLISHED
                      UDP   :::5353               *:*                       NONE
                      UDP   10.0.0.3:59925        *:*                       NONE
        threads       TID              USER          SYSTEM
                      11795             0.7            1.35
                      11796            0.68            1.37
                      15887            0.74            0.03
                      19055            0.77            0.01
                      [...]
                      total=47
        res-limits    RLIMIT                     SOFT       HARD
                      virtualmem             infinity   infinity
                      coredumpsize                  0   infinity
                      cputime                infinity   infinity
                      datasize               infinity   infinity
                      filesize               infinity   infinity
                      locks                  infinity   infinity
                      memlock                   65536      65536
                      msgqueue                 819200     819200
                      nice                          0          0
                      openfiles                  8192      65536
                      maxprocesses              63304      63304
                      rss                    infinity   infinity
                      realtimeprio                  0          0
                      rtimesched             infinity   infinity
                      sigspending               63304      63304
                      stack                   8388608   infinity
        mem-maps      RSS      PATH
                      381.4M   [anon]
                      62.8M    /opt/google/chrome/chrome
                      15.8M    /home/giampaolo/.config/google-chrome/Default/History
                      6.6M     /home/giampaolo/.config/google-chrome/Default/Favicons
                      [...]
        """

        import argparse
        import datetime
        import socket
        import sys

        import psutil
        from psutil._common import bytes2human

        ACCESS_DENIED = ''
        NON_VERBOSE_ITERATIONS = 4
        RLIMITS_MAP = {
            "RLIMIT_AS": "virtualmem",
            "RLIMIT_CORE": "coredumpsize",
            "RLIMIT_CPU": "cputime",
            "RLIMIT_DATA": "datasize",
            "RLIMIT_FSIZE": "filesize",
            "RLIMIT_LOCKS": "locks",
            "RLIMIT_MEMLOCK": "memlock",
            "RLIMIT_MSGQUEUE": "msgqueue",
            "RLIMIT_NICE": "nice",
            "RLIMIT_NOFILE": "openfiles",
            "RLIMIT_NPROC": "maxprocesses",
            "RLIMIT_RSS": "rss",
            "RLIMIT_RTPRIO": "realtimeprio",
            "RLIMIT_RTTIME": "rtimesched",
            "RLIMIT_SIGPENDING": "sigspending",
            "RLIMIT_STACK": "stack",
        }

        def print_(a, b):
            if sys.stdout.isatty() and psutil.POSIX:
                fmt = '\x1b[1;32m%-13s\x1b[0m %s' % (a, b)
            else:
                fmt = '%-11s %s' % (a, b)
            print(fmt)

        def str_ntuple(nt, convert_bytes=False):
            if nt == ACCESS_DENIED:
                return ""
            if not convert_bytes:
                return ", ".join(["%s=%s" % (x, getattr(nt, x)) for x in nt._fields])
            else:
                return ", ".join(["%s=%s" % (x, bytes2human(getattr(nt, x)))
                                  for x in nt._fields])

        def run(pid, verbose=False):
            try:
                proc = psutil.Process(pid)
                pinfo = proc.as_dict(ad_value=ACCESS_DENIED)
            except psutil.NoSuchProcess as err:
                sys.exit(str(err))

            # collect other proc info
            with proc.oneshot():
                try:
                    parent = proc.parent()
                    if parent:
                        parent = '(%s)' % parent.name()
                    else:
                        parent = ''
                except psutil.Error:
                    parent = ''
                try:
                    pinfo['children'] = proc.children()
                except psutil.Error:
                    pinfo['children'] = []
                if pinfo['create_time']:
                    started = datetime.datetime.fromtimestamp(
                        pinfo['create_time']).strftime('%Y-%m-%d %H:%M')
                else:
                    started = ACCESS_DENIED

            # here we go
            print_('pid', pinfo['pid'])
            print_('name', pinfo['name'])
            print_('parent', '%s %s' % (pinfo['ppid'], parent))
            print_('exe', pinfo['exe'])
            print_('cwd', pinfo['cwd'])
            print_('cmdline', ' '.join(pinfo['cmdline']))
            print_('started', started)

            cpu_tot_time = datetime.timedelta(seconds=sum(pinfo['cpu_times']))
            cpu_tot_time = "%s:%s.%s" % (
                cpu_tot_time.seconds // 60 % 60,
                str((cpu_tot_time.seconds % 60)).zfill(2),
                str(cpu_tot_time.microseconds)[:2])
            print_('cpu-tspent', cpu_tot_time)
            print_('cpu-times', str_ntuple(pinfo['cpu_times']))
            if hasattr(proc, "cpu_affinity"):
                print_("cpu-affinity", pinfo["cpu_affinity"])
            if hasattr(proc, "cpu_num"):
                print_("cpu-num", pinfo["cpu_num"])

            print_('memory', str_ntuple(pinfo['memory_info'], convert_bytes=True))
            print_('memory %', round(pinfo['memory_percent'], 2))
            print_('user', pinfo['username'])
            if psutil.POSIX:
                print_('uids', str_ntuple(pinfo['uids']))
            if psutil.POSIX:
                print_('uids', str_ntuple(pinfo['uids']))
            if psutil.POSIX:
                print_('terminal', pinfo['terminal'] or '')

            print_('status', pinfo['status'])
            print_('nice', pinfo['nice'])
            if hasattr(proc, "ionice"):
                try:
                    ionice = proc.ionice()
                except psutil.Error:
                    pass
                else:
                    if psutil.WINDOWS:
                        print_("ionice", ionice)
                    else:
                        print_("ionice", "class=%s, value=%s" % (
                            str(ionice.ioclass), ionice.value))

            print_('num-threads', pinfo['num_threads'])
            if psutil.POSIX:
                print_('num-fds', pinfo['num_fds'])
            if psutil.WINDOWS:
                print_('num-handles', pinfo['num_handles'])

            if 'io_counters' in pinfo:
                print_('I/O', str_ntuple(pinfo['io_counters'], convert_bytes=True))
            if 'num_ctx_switches' in pinfo:
                print_("ctx-switches", str_ntuple(pinfo['num_ctx_switches']))
            if pinfo['children']:
                template = "%-6s %s"
                print_("children", template % ("PID", "NAME"))
                for child in pinfo['children']:
                    try:
                        print_('', template % (child.pid, child.name()))
                    except psutil.AccessDenied:
                        print_('', template % (child.pid, ""))
                    except psutil.NoSuchProcess:
                        pass

            if pinfo['open_files']:
                print_('open-files', 'PATH')
                for i, file in enumerate(pinfo['open_files']):
                    if not verbose and i >= NON_VERBOSE_ITERATIONS:
                        print_("", "[...]")
                        break
                    print_('', file.path)
            else:
                print_('open-files', '')

            if pinfo['connections']:
                template = '%-5s %-25s %-25s %s'
                print_('connections',
                       template % ('PROTO', 'LOCAL ADDR', 'REMOTE ADDR', 'STATUS'))
                for conn in pinfo['connections']:
                    if conn.type == socket.SOCK_STREAM:
                        type = 'TCP'
                    elif conn.type == socket.SOCK_DGRAM:
                        type = 'UDP'
                    else:
                        type = 'UNIX'
                    lip, lport = conn.laddr
                    if not conn.raddr:
                        rip, rport = '*', '*'
                    else:
                        rip, rport = conn.raddr
                    print_('', template % (
                        type,
                        "%s:%s" % (lip, lport),
                        "%s:%s" % (rip, rport),
                        conn.status))
            else:
                print_('connections', '')

            if pinfo['threads'] and len(pinfo['threads']) > 1:
                template = "%-5s %12s %12s"
                print_('threads', template % ("TID", "USER", "SYSTEM"))
                for i, thread in enumerate(pinfo['threads']):
                    if not verbose and i >= NON_VERBOSE_ITERATIONS:
                        print_("", "[...]")
                        break
                    print_('', template % thread)
                print_('', "total=%s" % len(pinfo['threads']))
            else:
                print_('threads', '')

            if hasattr(proc, "rlimit"):
                res_names = [x for x in dir(psutil) if x.startswith("RLIMIT")]
                resources = []
                for res_name in res_names:
                    try:
                        soft, hard = proc.rlimit(getattr(psutil, res_name))
                    except psutil.AccessDenied:
                        pass
                    else:
                        resources.append((res_name, soft, hard))
                if resources:
                    template = "%-12s %15s %15s"
                    print_("res-limits", template % ("RLIMIT", "SOFT", "HARD"))
                    for res_name, soft, hard in resources:
                        if soft == psutil.RLIM_INFINITY:
                            soft = "infinity"
                        if hard == psutil.RLIM_INFINITY:
                            hard = "infinity"
                        print_('', template % (
                            RLIMITS_MAP.get(res_name, res_name), soft, hard))

            if hasattr(proc, "environ") and pinfo['environ']:
                template = "%-25s %s"
                print_("environ", template % ("NAME", "VALUE"))
                for i, k in enumerate(sorted(pinfo['environ'])):
                    if not verbose and i >= NON_VERBOSE_ITERATIONS:
                        print_("", "[...]")
                        break
                    print_("", template % (k, pinfo['environ'][k]))

            if pinfo.get('memory_maps', None):
                template = "%-8s %s"
                print_("mem-maps", template % ("RSS", "PATH"))
                maps = sorted(pinfo['memory_maps'], key=lambda x: x.rss, reverse=True)
                for i, region in enumerate(maps):
                    if not verbose and i >= NON_VERBOSE_ITERATIONS:
                        print_("", "[...]")
                        break
                    print_("", template % (bytes2human(region.rss), region.path))

        def main(argv=None):
            parser = argparse.ArgumentParser(
                description="print information about a process")
            parser.add_argument("pid", type=int, help="process pid")
            parser.add_argument('--verbose', '-v', action='store_true',
                                help="print more info")
            args = parser.parse_args()
            run(args.pid, args.verbose)

        sys.exit(main())
    def thg_command_iotop(self, *args, **kwargs):
        # !/usr/bin/env python

        # Copyright (c) 2009, Giampaolo Rodola'. All rights reserved.
        # Use of this source code is governed by a BSD-style license that can be
        # found in the LICENSE file.

        """
        A clone of iotop (http://guichaz.free.fr/iotop/) showing real time
        disk I/O statistics.

        It works on Linux only (FreeBSD and macOS are missing support for IO
        counters).
        It doesn't work on Windows as curses module is required.

        Example output:

        $ python scripts/iotop.py
        Total DISK READ: 0.00 B/s | Total DISK WRITE: 472.00 K/s
        PID   USER      DISK READ  DISK WRITE  COMMAND
        13155 giampao    0.00 B/s  428.00 K/s  /usr/bin/google-chrome-beta
        3260  giampao    0.00 B/s    0.00 B/s  bash
        3779  giampao    0.00 B/s    0.00 B/s  gnome-session --session=ubuntu
        3830  giampao    0.00 B/s    0.00 B/s  /usr/bin/dbus-launch
        3831  giampao    0.00 B/s    0.00 B/s  //bin/dbus-daemon --fork --print-pid 5
        3841  giampao    0.00 B/s    0.00 B/s  /usr/lib/at-spi-bus-launcher
        3845  giampao    0.00 B/s    0.00 B/s  /bin/dbus-daemon
        3848  giampao    0.00 B/s    0.00 B/s  /usr/lib/at-spi2-core/at-spi2-registryd
        3862  giampao    0.00 B/s    0.00 B/s  /usr/lib/gnome-settings-daemon

        Author: Giampaolo Rodola' <g.rodola@gmail.com>
        """

        import atexit
        import time
        import sys
        try:
            import curses
        except ImportError:
            sys.exit('platform not supported')

        import psutil
        from psutil._common import bytes2human

        def tear_down():
            win.keypad(0)
            curses.nocbreak()
            curses.echo()
            curses.endwin()

        win = curses.initscr()
        atexit.register(tear_down)
        curses.endwin()
        lineno = 0

        def print_line(line, highlight=False):
            """A thin wrapper around curses's addstr()."""
            global lineno
            try:
                if highlight:
                    line += " " * (win.getmaxyx()[1] - len(line))
                    win.addstr(lineno, 0, line, curses.A_REVERSE)
                else:
                    win.addstr(lineno, 0, line, 0)
            except curses.error:
                lineno = 0
                win.refresh()
                raise
            else:
                lineno += 1

        def poll(interval):
            """Calculate IO usage by comparing IO statics before and
            after the interval.
            Return a tuple including all currently running processes
            sorted by IO activity and total disks I/O activity.
            """
            # first get a list of all processes and disk io counters
            procs = [p for p in psutil.process_iter()]
            for p in procs[:]:
                try:
                    p._before = p.io_counters()
                except psutil.Error:
                    procs.remove(p)
                    continue
            disks_before = psutil.disk_io_counters()

            # sleep some time
            time.sleep(interval)

            # then retrieve the same info again
            for p in procs[:]:
                with p.oneshot():
                    try:
                        p._after = p.io_counters()
                        p._cmdline = ' '.join(p.cmdline())
                        if not p._cmdline:
                            p._cmdline = p.name()
                        p._username = p.username()
                    except (psutil.NoSuchProcess, psutil.ZombieProcess):
                        procs.remove(p)
            disks_after = psutil.disk_io_counters()

            # finally calculate results by comparing data before and
            # after the interval
            for p in procs:
                p._read_per_sec = p._after.read_bytes - p._before.read_bytes
                p._write_per_sec = p._after.write_bytes - p._before.write_bytes
                p._total = p._read_per_sec + p._write_per_sec

            disks_read_per_sec = disks_after.read_bytes - disks_before.read_bytes
            disks_write_per_sec = disks_after.write_bytes - disks_before.write_bytes

            # sort processes by total disk IO so that the more intensive
            # ones get listed first
            processes = sorted(procs, key=lambda p: p._total, reverse=True)

            return (processes, disks_read_per_sec, disks_write_per_sec)

        def refresh_window(procs, disks_read, disks_write):
            """Print results on screen by using curses."""
            curses.endwin()
            templ = "%-5s %-7s %11s %11s  %s"
            win.erase()

            disks_tot = "Total DISK READ: %s | Total DISK WRITE: %s" \
                        % (bytes2human(disks_read), bytes2human(disks_write))
            print_line(disks_tot)

            header = templ % ("PID", "USER", "DISK READ", "DISK WRITE", "COMMAND")
            print_line(header, highlight=True)

            for p in procs:
                line = templ % (
                    p.pid,
                    p._username[:7],
                    bytes2human(p._read_per_sec),
                    bytes2human(p._write_per_sec),
                    p._cmdline)
                try:
                    print_line(line)
                except curses.error:
                    break
            win.refresh()

        def main():
            try:
                interval = 0
                while True:
                    args = poll(interval)
                    refresh_window(*args)
                    interval = 1
            except (KeyboardInterrupt, SystemExit):
                pass

        main()
    def thg_command_killall(self, *args, **kwargs):
        # !/usr/bin/env python

        # Copyright (c) 2009, Giampaolo Rodola'. All rights reserved.
        # Use of this source code is governed by a BSD-style license that can be
        # found in the LICENSE file.

        """
        Kill a process by name.
        """

        import os
        import sys
        import psutil

        def main():
            if len(sys.argv) != 2:
                sys.exit('usage: %s name' % __file__)
            else:
                NAME = sys.argv[1]

            killed = []
            for proc in psutil.process_iter():
                if proc.name() == NAME and proc.pid != os.getpid():
                    proc.kill()
                    killed.append(proc.pid)
            if not killed:
                sys.exit('%s: no process found' % NAME)
            else:
                sys.exit(0)


        main()







