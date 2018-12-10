from __future__ import print_function

import atexit
import itertools
import os
import sys
import traceback
import socket,platform
from collections import Counter
from colorama import Fore
from future.builtins import input
from time import sleep
from thgconsole.config.Version import __codenome__,__version__
from thgconsole.core.CoreUtils.exceptions import THGtException
from glob import glob
from thgconsole.core.CoreUtils.utils import (
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
from thgconsole.core.CoreUtils.printer import (
    print_info,
    print_success,
    print_error,
    print_status,
    print_table,
    pprint_dict_in_order,
    PrinterThread,
    printer_queue
)
from thgconsole.core.ModulesBuild.Exploits.exploit import GLOBAL_OPTS
from thgconsole.core.ModulesBuild.Payloads.payloads import BasePayload

import readline


def is_libedit():
    return "libedit" in readline.__doc__


class BaseInterpreter(object):
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
        """ Split line into command and argument.

        :param line: line to parse
        :return: (command, argument)
        """
        command, _, arg = line.strip().partition(" ")
        return command, arg.strip()

    @property
    def prompt(self):
        """ Returns prompt string """
        return ">>>"

    def get_command_handler(self, command):
        """ Parsing command and returning appropriate handler.

        :param command: command
        :return: command_handler
        """
        try:
            command_handler = getattr(self, "command_{}".format(command))
        except AttributeError:
            raise THGtException("Unknown command: '{}'".format(command))

        return command_handler

    def start(self):
        """ Routersploit main entry point. Starting interpreter loop. """

        print_info(self.banner)
        printer_queue.join()
        while True:
            try:
                command, args = self.parse_line(input(self.prompt))
                if not command:
                    continue
                command_handler = self.get_command_handler(command)
                command_handler(args)
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

        If a command has not been entered, then complete against command list.
        Otherwise try to call complete_<command> to get list of completions.
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
                complete_function = self.raw_command_completer

            self.completion_matches = complete_function(text, line, start_index, end_index)

        try:
            return self.completion_matches[state]
        except IndexError:
            return None

    def commands(self, *ignored):
        """ Returns full list of interpreter commands.

        :param ignored:
        :return: full list of interpreter commands
        """
        return [command.rsplit("_").pop() for command in dir(self) if command.startswith("command_")]

    def raw_command_completer(self, text, line, start_index, end_index):
        """ Complete command w/o any argument """
        return [command for command in self.suggested_commands() if command.startswith(text)]

    def default_completer(self, *ignored):
        return []

    def suggested_commands(self):
        """ Entry point for intelligent tab completion.

        Overwrite this method to suggest suitable commands.

        :return: list of suitable commands
        """
        return self.commands()


class THGtInterpreter(BaseInterpreter):
    history_file = os.path.expanduser("~/.THG_history")
    global_help = """
\033[0;32mGlobal commands:

#Alias Commands
==============

Command       Description
-------       -----------
#alias         create or view an alias.
#del           rm
#handler       use exploit/multi/handler

Core Commands
=============

    Command       Description
    -------       -----------
    show banner    Display an awesome thgbanner
    show Ip        show internal ip 
    exit           Exit the console
    unsetg         Unsets one or more global variables
    help           Help menu
    show history   Show command history
    setg           Sets a global variable to a value
    set            Sets a context-specific variable to a value
    exec           <shell command> <args> Execute a command in a shell
    cd             Change the current working directory
    color          Toggle color
    route          Route traffic through a session V-1base
    show version   Show the framework and console library version numbers
    quit           Exit the console
    #connect       Communicate with a host
    #get           Gets the value of a context-specific variable
    #getg          Gets the value of a global variable
    #grep          Grep the output of another command
    #load          Load a framework plugin
    #save          Saves the active datastores
    #sessions      Dump session listings and display information about sessions
    sleep         Do nothing for the specified number of seconds
    #spool         Write console output into a file as well the screen
    #unload        Unload a framework plugin
    #unset         Unsets one or more context-specific variables



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
#makerc        Save commands entered since start to a file
#resource      Run the commands stored in a file

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
    """.format(Blue=Fore.CYAN,grn=Fore.GREEN,red=Fore.RED,yl=Fore.YELLOW,magent=Fore.MAGENTA)

    module_help = """
    \033[1;34mModule commands:
    run                                 Run the selected module with the given options
    back                                De-select the current module
    set <option name> <option value>    Set an option for the selected module
    setg <option name> <option value>   Set an option for all of the modules
    unsetg <option name>                Unset option that was set globally
    show [info|options|devices]         Print information, options, or target devices for a module
    check                               Check if a given target is vulnerable to a selected module's exploit"""

    def __init__(self,extra_package_path=None):
        super(THGtInterpreter, self).__init__()
        PrinterThread().start()

        self.current_module = None
        self.raw_prompt_template = None
        self.module_prompt_template = None
        self.prompt_hostname = "\033[0;32mPWN"
        self.show_sub_commands =sorted(("info",
                                  "Eip",
                                  "Ip",
                                  "history",
                                  "options",
                                  "devices",
                                  "all",
                                  "encoders",
                                  "creds",
                                  "exploits",
                                  "scanners",#mudar explit e tall
                                  "wordlists",
                                  "banner",
                                  "version"
                                        ))

        self.global_commands = sorted(["use",
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
                                       "sleep"

                                       ])
        self.module_commands = ["run", "back", "set ", "setg ", "check"]
        self.module_commands.extend(self.global_commands)
        self.module_commands.sort()
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

        self.__parse_prompt()
        self.ran = """
          \033[1;31m████████╗██╗  ██╗███████╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗      ██████╗ ██████╗  ██████╗ ██╗   ██╗██████╗ 
        ╚══██╔══╝██║  ██║██╔════╝    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ██╔════╝ ██╔══██╗██╔═══██╗██║   ██║██╔══██╗
           ██║   ███████║█████╗      ███████║███████║██║     █████╔╝ █████╗  ██████╔╝    ██║  ███╗██████╔╝██║   ██║██║   ██║██████╔╝
           ██║   ██╔══██║██╔══╝      ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗    ██║   ██║██╔══██╗██║   ██║██║   ██║██╔═══╝ 
           ██║   ██║  ██║███████╗    ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║    ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║     
           ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     
        \033[1;34m                         

        """
        self.banner = """
{CYAN}==================={GREEN}[ thgconsole {version} ]{GREEN}{CYAN}===================

{YELLOW}+ -- --=[{RED}THGEF   :{MAGENTA} The Hacker Group Exploitation Framework{RED}{YELLOW}]=-- -- +    
{YELLOW}+ -- --=[{RED}Code by :{MAGENTA} Darkcode                               {RED}{YELLOW}]=-- -- + 
{YELLOW}+ -- --=[{RED}Codename:{MAGENTA} {codenome}                                {RED}{YELLOW}]=-- -- + 
{YELLOW}+ -- --=[{RED}Homepage:{MAGENTA} https://www.facebook.com/darckode0x00/ {RED}{YELLOW}]=-- -- + 
{YELLOW}+ -- --=[{RED}youtube :{MAGENTA} darkcode programming                   {RED}{YELLOW}]=-- -- + 

{CYAN}==================={GREEN}[ thgconsole-pc ]{GREEN}{CYAN}========================

{YELLOW}+ -- --=[{RED}system  =>{MAGENTA} {os}   {RED}{YELLOW}]=-- -- + 
{YELLOW}+ -- --=[{RED}machine =>{MAGENTA} {machine}  {RED}{YELLOW}]=-- -- +      

{CYAN}==================={GREEN}[ thgconsole-info ]{GREEN}{CYAN}========================
 
{YELLOW}+ -- --=[{RED}Exploits {MAGENTA} {exploits_count}  {RED}{YELLOW}]=-- -- +  
{YELLOW}+ -- --=[{RED}Auxiliary{MAGENTA} {auxiliary_count} {RED}{YELLOW}]=-- -- + 
{YELLOW}+ -- --=[{RED}Post     {MAGENTA} {post_count}      {RED}{YELLOW}]=-- -- + 
{YELLOW}+ -- --=[{RED}Payloads {MAGENTA} {payloads_count}  {RED}{YELLOW}]=-- -- + 
{YELLOW}+ -- --=[{RED}Encoders {MAGENTA} {encoders_count}  {RED}{YELLOW}]=-- -- + 
{YELLOW}+ -- --=[{RED}Nops     {MAGENTA} {nops_count}      {RED}{YELLOW}]=-- -- + 


        """.format(os=platform.uname()[0],
                   release=platform.uname()[2],
                   versao=platform.uname()[3],
                   machine=platform.uname()[4],
                   processor=platform.uname()[5],
                   hostname=platform.uname()[1],
                   exploits_count=self.modules_count["exploits"]+ self.modules_count['extra_exploits'],
                   encoders_count=self.modules_count["encoders"] + self.modules_count['extra_encoders'],
                   auxiliary_count=self.modules_count["auxiliary"] + self.modules_count['extra_auxiliary'],
                   nops_count=self.modules_count["nops"]+ self.modules_count['extra_nops'],
                   payloads_count=self.modules_count["payloads"]+ self.modules_count['extra_payloads'],
                   post_count=self.modules_count["post"]+ self.modules_count['extra_post'],
                   codenome = __codenome__,
                   version = __version__,
                   CYAN=Fore.CYAN,
                   GREEN=Fore.GREEN,
                   RED=Fore.RED,
                   YELLOW=Fore.YELLOW,
                   MAGENTA=Fore.MAGENTA)

    def ipi(self, darkcde):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        a = s.getsockname()[0]
        return a

    def __parse_prompt(self):
        raw_prompt_default_template = "\001\033[4m\002{host}\001\033[0m\002 > "
        raw_prompt_template = os.getenv("THG_RAW_PROMPT", raw_prompt_default_template).replace('\\033', '\033')
        self.raw_prompt_template = raw_prompt_template if '{host}' in raw_prompt_template else raw_prompt_default_template

        module_prompt_default_template = "\001\033[4m\002{host}\001\033[0m\002 (\001\033[91m\002{module}\001\033[0m\002) > "
        module_prompt_template = os.getenv("THG_MODULE_PROMPT", module_prompt_default_template).replace('\\033', '\033')
        self.module_prompt_template = module_prompt_template if all(map(lambda x: x in module_prompt_template, ['{host}', "{module}"])) else module_prompt_default_template

    @property
    def module_metadata(self):
        return getattr(self.current_module, "_{}__info__".format(self.current_module.__class__.__name__))

    @property
    def prompt(self):
        """ Returns prompt string based on current_module attribute.

        Adding module prefix (module.name) if current_module attribute is set.

        :return: prompt string with appropriate module prefix.
        """
        if self.current_module:
            try:
                return self.module_prompt_template.format(host=self.prompt_hostname, module=self.module_metadata['name'])
            except (AttributeError, KeyError):
                return self.module_prompt_template.format(host=self.prompt_hostname, module="UnnamedModule")
        else:
            return self.raw_prompt_template.format(host=self.prompt_hostname)

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

        :param text: argument of 'use' command
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

    def suggested_commands(self):
        """ Entry point for intelligent tab completion.

        Based on state of interpreter this method will return intelligent suggestions.

        :return: list of most accurate command suggestions
        """
        if self.current_module and GLOBAL_OPTS:
            return sorted(itertools.chain(self.module_commands, ("unsetg ",)))
        elif self.current_module:
            return self.module_commands
        else:
            return self.global_commands

    def command_back(self, *args, **kwargs):
        self.current_module = None

    def command_use(self, module_path, *args, **kwargs):
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
    def command_run(self, *args, **kwargs):
        print_status("Running module...")
        try:
            self.current_module.run()
        except KeyboardInterrupt:
            print_info()
            print_error("Operation cancelled by user")
        except Exception:
            print_error(traceback.format_exc(sys.exc_info()))

    def command_exploit(self, *args, **kwargs):
        self.command_run()

    @module_required
    def command_set(self, *args, **kwargs):
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
    def command_setg(self, *args, **kwargs):
        kwargs['glob'] = True
        self.command_set(*args, **kwargs)


    @stop_after(2)
    def complete_setg(self, text, *args, **kwargs):
        return self.complete_set(text, *args, **kwargs)

    @module_required
    def command_unsetg(self, *args, **kwargs):
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

        print_table(headers, *wordlists, max_column_length=100)


    @module_required
    def _show_encoders(self, *args, **kwargs):
        if issubclass(self.current_module.__class__, BasePayload):
            encoders = self.current_module.get_encoders()
            if encoders:
                headers = ("Encoder", "Name", "Description")
                print_table(headers, *encoders, max_column_length=100)
                return

        print_error("No encoders available")

    def __show_modules(self, root=''):
        for module in [module for module in self.modules if module.startswith(root)]:
            print_info(module.replace('.', os.sep))

    def _show_all(self, *args, **kwargs):
        self.__show_modules()

    def _show_scanners(self, *args, **kwargs):
        self.__show_modules('scanners')

    def _show_test(self, *args, **kwargs):
        self.__show_modules('test')

    def _show_exploits(self, *args, **kwargs):
        self.__show_modules('exploits')

    def _show_payloads(self, *args, **kwargs):
        self.__show_modules('payloads')

    def _show_creds(self, *args, **kwargs):
        self.__show_modules('creds')

    def _show_banner(self, *args, **kwargs):
        os.system("clear")
        print(self.banner)

    def _show_version(self, *args, **kwargs):
        print_status(__codenome__+"-"+__version__)
    def _show_Ip(self, *args, **kwargs):
        print(self.ipi(darkcde=None))

    # def _show_Eip(self,*args,**kwargs):
    # print(ipgetter.myip())
    def _show_history(self, *args, **kwargs):
        os.system("cat ~/.THG_history")
    def command_show(self, *args, **kwargs):
        sub_command = args[0]
        try:
            getattr(self, "_show_{}".format(sub_command))(*args, **kwargs)
        except AttributeError:
            print_error("Unknown 'show' sub-command '{}'. "
                        "What do you want to show?\n"
                        "Possible choices are: {}".format(sub_command, self.show_sub_commands))
    @stop_after(2)
    def complete_show(self, text, *args, **kwargs):
        if text:
            return [command for command in self.show_sub_commands if command.startswith(text)]
        else:
            return self.show_sub_commands
    @module_required
    def command_check(self, *args, **kwargs):
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
    def command_sleep(self,args, **kwargs):
        print_success("sleep "+str(args))
        sleep(float(args))
    def command_help(self, *args, **kwargs):
        print_info(self.global_help)
        if self.current_module:
            print_info("\n", self.module_help)
    def command_log(self,*args,**kwargs):
        os.system("cat thgconsole.log")
    def command_exec(self, *args, **kwargs):
        os.system(args[0])
    def command_shell(self,*args, **kwargs):
        os.system("bash")
    def command_color(self,args,**kwargs):
        self.prompt_hostname = args
    def command_python_interpreter(self,*args, **kwargs):
        os.system("python3")
    def command_route(self,args,**kwargs):
        os.system("route "+args)
    def command_cd(self,*args,**kwargs):
        dir = os.getcwd()
        try:
            heck =  os.path.exists(args[0])

            total = glob(args[0]+"/*")
            print_status("current: "+dir)
            if args[0] == "":
                pass
            else:
                changer_dir = os.chdir(args[0])
                dir = os.getcwd()
                directories = [d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]
                file = [d for d in os.listdir(os.getcwd()) if os.path.isfile(d)]
                print_status("change: "+dir)
                print_status("total:"+str(len(total))+" FILE:"+str(len(file))+" FOLDER:"+str(len(directories)))
                arquivos = []
                pastas = []
                for i in glob("*"):
                    if os.path.isdir(i) == True:
                        print(Fore.CYAN+i+Fore.LIGHTYELLOW_EX+"/")

                    else:
                        print(Fore.RED+i)
        except:
            pass

    def command_quit(self, *args,**kwargs):
        print_status("thgconsole stopped")
        exit(1)
    def command_search(self, *args, **kwargs):
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

    def command_exit(self, *args, **kwargs):
        raise EOFError