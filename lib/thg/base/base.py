import argparse
from io import BytesIO
from queue import Queue
from lib.thg.thgcmd import *
from lib.thg.thgcmd.ansi import style
from lib.thg.thgcmd.utils import  basic_complete
from art import text2art
from pathlib import Path
from lib.thg.thgcmd.ansi import style
from tabulate import tabulate
from colorama import Fore
from random import *
from lib.thg.base import plugins
from lib.thg.base.config.mensagens import mensagem_do_dia
import psutil,os,platform
from lib.thg.base.config.Version import __codenome__,__version__
from lib.thg.base.config.info_init import thg_add_init
from importlib import import_module, reload
from lib.thg.core.Database.Database import Database
from lib.thg.base.BaseOptions import BaseOption
from lib.thg.base.exception.Module import ModuleNotUseException
import sys, time, pkgutil, threading, json


class THGBASECONSOLE(Cmd, Database):
    #__metaclass__ = Database
    colors = "Always"
    console_prompt = "{COLOR_START}thg-console{COLOR_END}".format(COLOR_START=Fore.CYAN, COLOR_END=Fore.BLUE)
    console_prompt_end = " > "
    module_name = None
    module_class = None
    module_instance = None

    # command categories
    CMD_CORE = "Core Command"
    CMD_MODULE = "Module Command"
    CMD_DATABASE= "Database Backend Commands"
    CMD_SYSTEM= "SYSTEM Commands"
    CMD_PLUGINS = "Plugins Commands"

    def __init__(self):
        shortcuts = dict()
        shortcuts.update({'add': 'commandos longos do thg'})
        alias_script = os.path.join(os.path.dirname(__file__), '.cmd2rc')
        super(THGBASECONSOLE, self).__init__(startup_script=alias_script,
                                             use_ipython=True,
                                             completekey="tab",
                                             persistent_history_file="history",
                                              persistent_history_length=999999,
                                             multiline_commands=['orate'],
                                             shortcuts=shortcuts,
                                             )

        self.locals_in_py = True
        self.debug = True
        self.editor = "nano"
        self.allow_redirection = False
        self.allow_cli_args = False
        Database.__init__(Database)
        self.prompt = self.console_prompt + self.console_prompt_end
        self.thgcmd_banner(None)
        secure_random = SystemRandom()
        item = secure_random.choice(mensagem_do_dia)
        print("\n"+Fore.RED+"'''"+item+"'''"+"\n")
        self.loadedPlugins = {}
        self.resourceQueue = []

    '''
     # command categories
    CMD_CORE = "Core Command"
    CMD_MODULE = "Module Command"
    CMD_DATABASE= "Database Backend Commands"
    '''

    @with_category(CMD_PLUGINS)
    def thgcmd_plugins(self, args):
        "List all available and active plugins."
        pluginPath = os.path.abspath("plugins")
        print(Fore.RED+"[*] Searching for plugins at {}".format(pluginPath))
        # From walk_packages: "Note that this function must import all packages
        # (not all modules!) on the given path, in order to access the __path__
        # attribute to find submodules."
        pluginNames = [name for _, name, _ in pkgutil.walk_packages([pluginPath])]
        numFound = len(pluginNames)
        print(numFound)

        # say how many we found, handling the 1 case
        if numFound == 1:
            print(Fore.RED+"[*] {} plugin found".format(numFound))
        else:
            print(Fore.RED+"[*] {} plugins found".format(numFound))

        # if we found any, list them
        if numFound > 0:
            print("\tName\tActive")
            print("\t----\t------")
            activePlugins = self.loadedPlugins.keys()
            for name in pluginNames:
                active = ""
                if name in activePlugins:
                    active = "******"
                print("\t" + name + "\t" + active)

        print("")
        print(Fore.RED+"[*] Use \"plugin <plugin name>\" to load a plugin.")

    @with_category(CMD_PLUGINS)
    def thgcmd_plugin(self, pluginName):
        "Load a plugin file to extend thg."
        pluginPath = os.path.abspath("plugins")
        print(Fore.RED+"[*] Searching for plugins at {}".format(pluginPath))
        # From walk_packages: "Note that this function must import all packages
        # (not all modules!) on the given path, in order to access the __path__
        # attribute to find submodules."
        pluginNames = [name for _, name, _ in pkgutil.walk_packages([pluginPath])]
        if pluginName in pluginNames:
            print(Fore.RED+"[*] Plugin {} found.".format(pluginName))

            message = "[*] Loading plugin {}".format(pluginName)
            signal = json.dumps({
                'print': True,
                'message': message
            })

            # 'self' is the mainMenu object
            plugins.load_plugin(self, pluginName)
        else:
            raise Exception("[!] Error: the plugin specified does not exist in {}.".format(pluginPath))

    @with_category(CMD_CORE)
    def thgcmd_banner(self, args):
        # self.module_class.Exploits_count=self.modules_count["exploits"] + self.modules_count['extra_exploits'],
        # encoders_count=self.modules_count["encoders"] + self.modules_count['extra_encoders'],
        # auxiliary_count=self.modules_count["auxiliary"] + self.modules_count['extra_auxiliary'],
        # nops_count=self.modules_count["nops"] + self.modules_count['extra_nops'],
        # payloads_count=self.modules_count["payloads"] + self.modules_count['extra_payloads'],
        # post_count=self.modules_count["post"] + self.modules_count['extra_post'],
        #                    evasion_count=self.modules_count["evasion"],
        """Print thg-console bannercolor_end=Fore.RESETlistmod"""
        ascii_text = text2art("thg-console", "rand")
        self.poutput("\n\n")
        #self.poutput(ascii_text, '\n\n', color=Fore.LIGHTCYAN_EX)
        #self.poutput("thg-console has {count} modules".format(count=self.get_module_count()), "\n\n", color=Fore.MAGENTA)
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
        {YELLOW}+ -- --=[{RED}ip      =>{MAGENTA} {ip}       {RED}{YELLOW}]=-- -- +
        {YELLOW}+ -- --=[{RED}mac     =>{MAGENTA} {mac} {RED}{YELLOW}]=-- -- +

        {CYAN}==================={GREEN}[ thgconsole-info ]{GREEN}{CYAN}========================
        {CYAN}==================={GREEN}[ thgconsole-config ]{GREEN}{CYAN}========================
        {YELLOW}+ -- --=[{RED}DB_STATUS =>{MAGENTA}on{RED}{YELLOW}]=-- -- +
                """.format(os=platform.uname()[0],
                           release=platform.uname()[2],
                           versao=platform.uname()[3],
                           machine=platform.uname()[4],
                           processor=platform.uname()[5],
                           hostname=platform.uname()[1],
                           codenome=__codenome__,
                           version=__version__,
                           CYAN=Fore.CYAN,
                           GREEN=Fore.GREEN,
                           RED=Fore.RED,
                           YELLOW=Fore.YELLOW,
                           MAGENTA=Fore.MAGENTA,
                           gccv=thg_add_init.check_gcc_version(),
                           python=thg_add_init.check_python_version(),
                           ip=thg_add_init.ipi(),
                           mac=thg_add_init.get_mac())
        print(self.banner)


    @with_category(CMD_CORE)
    def thgcmd_version(self,args):
        """show version"""
        if args == "all":
            self._print_item(__version__+" "+__codenome__)
        if args == "codenome":
            self._print_item(__codenome__)
        if args =="version":
            self._print_item(__version__)
        if args == "":
            self._print_item("help")
        if args =="help":
            self._print_item("all => show version+codenome")
            self._print_item("codenome => show codenome")
            self._print_item("version => show version")
    @with_category(CMD_CORE)
    def thgcmd_ip(self,args):
        """show ip"""
        if args == "external":
            self._print_item("send pycurl request...")
            import pycurl
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://ident.me')
            buffer = BytesIO()
            c.setopt(c.WRITEDATA, buffer)
            c.perform()
            # ok
            # Decode the response body:
            string_body = buffer.getvalue().decode('utf-8')
            self._print_item(str(string_body))

        elif args =="internal":
            self._print_item(thg_add_init.ipi())
        elif args == "help":
            self._print_item("external => show external ip ")
            self._print_item("internal => show internal ip ")
    #@with_category(CMD_CORE)
    #def thgcmd_exit(self,args):
    #    """Exit the console"""
    #    exit(1)
    @with_category(CMD_CORE)
    def thgcmd_exec(self,args):
        """ <shell thg_command> <args> Execute a thg_command in a shell"""
        os.system(args)
    @with_category(CMD_MODULE)
    def thgcmd_listmod(self, args):
        """List all modules"""
        local_modules = module.get_local_modules()
        self._print_modules(local_modules, "Module List:")

    @with_category(CMD_MODULE)
    def thgcmd_search(self, args):
        """
        Search modules

        Support fields:
            module_name, description, author, disclosure_date, service_name, service_version, check
        Eg:
            search redis
            search service_name=phpcms  service_version=9.6.0
        """
        search_args = args.split(" ")
        if len(search_args) < 2:
            print("You need to specify the type of search and the name.")
            print("Usage: search 'type' 'module_name'")
            print("Ex.: search auxiliary module_name")
            return
        search_type = search_args[0]
        search_type = search_type.lower()
        search_query = search_args[1]
        db_conditions = {}
        if search_type == "auxiliary":
            search = self.search_modules(search_query)
            if(search == []):
                modules = search
                fields = search
            else:
                modules = search[0]
                fields = search[1]

            self._print_modules(modules, fields, 'Search results for : ' + Fore.BLUE + search_query )
            #self._print_item("search mod => module_name, description, author, disclosure_date, service_name, service_version, check")
            #self._print_item("The search is only retrieved from the database")
            #self._print_item("If you add/delete some new modules, please execute `db_rebuild` first\n\n")

    def complete_set(self, text, line, begidx, endidx):
        if len(line.split(" ")) > 2:
            completion_items = []
        else:
            completion_items = ['debug']
            if self.module_instance:
                completion_items += [option.name for option in self.module_instance.options.get_options()]
        return basic_complete(text, line, begidx, endidx, completion_items)

    set_parser = argparse.ArgumentParser()
    set_parser.add_argument("name", help="The name of the field you want to set")
    set_parser.add_argument("-f", "--file", action="store_true", help="Specify multiple targets")
    set_parser.add_argument("value", help="The value of the field you want to set")

    @with_argparser(set_parser)
    @with_category(CMD_MODULE)
    def thgcmd_set(self, args):
        """Set module option value/ set program config"""
        if args.name == 'debug':
            self.debug = args.value
            return None

        if not self.module_instance:
            raise ModuleNotUseException()
        if args.file and args.name in ["HOST", "URL"]:
            try:
                open(args.value, 'r')
                self.module_instance.multi_target = True
            except IOError as e:
                self._print_item(e, color=Fore.RED)
                return False
        elif not args.file and args.name in ["HOST", "URL"]:
            self.module_instance.multi_target = False
            self.module_instance.targets = None

        self.module_instance.options.set_option(args.name, args.value)

    def complete_use(self, text, line, begidx, endidx):
        if len(line.split(" ")) > 2:
            modules = []
        else:
            modules = [local_module[0] for local_module in module.get_local_modules()]
        return basic_complete(text, line, begidx, endidx, modules)

    @with_category(CMD_MODULE)
    def thgcmd_use(self, module_name, module_reload=False):
        """Chose a module"""
        module_file = module.name_convert(module_name)
        module_type = module_name.split("/")[0]

        if Path(module_file).is_file():
            self.module_name = module_name
            if module_reload:
                self.module_class = reload(self.module_class)
            else:
                self.module_class = import_module("modules.{module_name}".format(module_name=module_name.replace("/", ".")))
            self.module_instance = self.module_class.Modules()
            self.set_prompt(module_type=module_type, module_name=module_name)
        else:
            self.poutput("Module/Exploit not found.")

    @with_category(CMD_MODULE)
    def thgcmd_back(self, args):
        """Clear module that chose"""
        self.module_name = None
        self.module_instance = None
        self.prompt = self.console_prompt + self.console_prompt_end

    def complete_show(self, text, line, begidx, endidx):
        if len(line.split(" ")) > 2:
            completion_items = []
        else:
            completion_items = ['info', 'options', 'missing']
        return basic_complete(text, line, begidx, endidx, completion_items)

    @with_category(CMD_MODULE)
    def thgcmd_show(self, content):
        """
        Display module information

        Eg:
            show info
            show options
            show missing
        """
        if not self.module_instance:
            raise ModuleNotUseException()

        if content == "info":
            info = self.module_instance.get_info()
            info_table = []
            self.poutput(style("Module info:"))
            for item in info.keys():
                info_table.append([item + ":", info.get(item)])
            self.poutput(tabulate(info_table, colalign=("right",), tablefmt="plain"), )

        if content == "options" or content == "info":
            options = self.module_instance.options.get_options()
            default_options_instance = BaseOption()
            options_table = []
            for option in options:
                options_table_row = []
                for field in default_options_instance.__dict__.keys():
                    options_table_row.append(getattr(option, field))
                options_table.append(options_table_row)

            self.poutput(style("Module options:",fg="red"))
            self.poutput(style(tabulate(options_table,headers=default_options_instance.__dict__.keys(),),fg="red"))

        if content == "missing":
            missing_options = self.module_instance.get_missing_options()
            if len(missing_options) is 0:
                self.poutput(style("No option missing!"))
                return None

            default_options_instance = BaseOption()
            missing_options_table = []
            for option in missing_options:
                options_table_row = []
                for field in default_options_instance.__dict__.keys():
                    options_table_row.append(getattr(option, field))
                missing_options_table.append(options_table_row)
            self.poutput(style("Missing Module options:"))
            self.poutput(style(tabulate(missing_options_table,headers=default_options_instance.__dict__.keys(),),))

    @with_category(CMD_MODULE)
    def thgcmd_run(self, args):
        """alias to exploit"""
        self.thgcmd_exploit(args=args)

    def exploit_thread(self, target, target_type, thread_queue):
        target_field = None
        port = None

        if target_type == "tcp":
            [target, port] = module.parse_ip_port(target)
            target_field = "HOST"
        elif target_type == "http":
            target_field = "URL"
        exp = self.module_class.Modules()
        exp.options.set_option(target_field, target)
        exp.options.set_option("TIMEOUT", self.module_instance.options.get_option("TIMEOUT"))
        if port:
            exp.options.set_option("PORT", port)
        else:
            exp.options.set_option("PORT", self.module_instance.options.get_option("PORT"))

        exploit_result = exp.exploit()

        if exploit_result.status:
            self._print_item(exploit_result.success_message)
        else:
            self._print_item(exploit_result.error_message)
        thread_queue.get(1)

    @with_category(CMD_MODULE)
    def thgcmd_exploit(self, args):
        """Execute module exploit"""
        if not self.module_instance:
            raise ModuleNotUseException()

        [validate_result, validate_message] = self.module_instance.options.validate()
        if not validate_result:
            for error in validate_message:
                self._print_item(error)
            return False


        if self.module_instance.multi_target:

            target_type = self.module_instance.target_type
            target_field = None

            if target_type == "tcp":
                target_field = "HOST"
            elif target_type == "http":
                target_field = "URL"

            target_filename = self.module_instance.options.get_option(target_field)

            try:
                target_file = open(target_filename, 'r')
                self.module_instance.targets = []
                for line in target_file.readlines():
                    self.module_instance.targets.append(line.strip())
                self.module_instance.multi_target = True
            except IOError as e:
                self._print_item(e, color=Fore.RED)
                return False


            targets = self.module_instance.targets
            targets_queue = Queue()
            for target in targets:
                targets_queue.put(target)


            if not targets_queue.empty():
                thread_count = int(self.module_instance.options.get_option("THREADS"))
                thread_queue = Queue(maxsize=thread_count)

                try:
                    while not targets_queue.empty():
                        while thread_queue.full():
                            time.sleep(0.1)

                        target = targets_queue.get()
                        thread_queue.put(1)
                        _thread = threading.Thread(target=self.exploit_thread, args=(target, target_type, thread_queue))
                        _thread.start()

                    while not thread_queue.empty():
                        time.sleep(0.1)
                except KeyboardInterrupt:
                    self._print_item("Wait for existing process to exit...", color=Fore.RED)
                    while threading.activeCount() > 1:
                        time.sleep(0.5)
                    return None

            self.poutput("{style}[*]{style_end} module execution completed".format(
                style=Fore.BLUE + Style.BRIGHT,
                style_end=Style.RESET_ALL
            ))
            return False

        exploit_result = self.module_instance.exploit()
        if exploit_result.status:
            self._print_item("module success!")
            self._print_item(exploit_result.success_message)
        else:
            self._print_item("module failure!", color=Fore.RED)
            self._print_item(exploit_result.error_message, color=Fore.RED)
        self.poutput("{style}[*]{style_end} module execution completed".format(
            style=Fore.BLUE + Style.BRIGHT,
            style_end=Style.RESET_ALL
        ))

    def check_thread(self, target, target_type, thread_queue):
        target_field = None
        port = None

        if target_type == "tcp":
            [target, port] = module.parse_ip_port(target)
            target_field = "HOST"
        elif target_type == "http":
            target_field = "URL"
        exp = self.module_class.Modules()
        exp.options.set_option(target_field, target)
        exp.options.set_option("TIMEOUT", self.module_instance.options.get_option("TIMEOUT"))
        if port:
            exp.options.set_option("PORT", port)
        else:
            exp.options.set_option("PORT", self.module_instance.options.get_option("PORT"))

        exploit_result = exp.check()

        if exploit_result.status:
            self._print_item(exploit_result.success_message)
        else:
            self._print_item(exploit_result.error_message, color=Fore.RED)
        thread_queue.get(1)

    @with_category(CMD_MODULE)
    def thgcmd_check(self, args):
        """Execute module check"""
        if not self.module_instance:
            raise ModuleNotUseException()

        [validate_result, validate_message] = self.module_instance.options.validate()
        if not validate_result:
            for error in validate_message:
                self._print_item(error, Fore.RED)
            return False

        if self.module_instance.multi_target:
            target_type = self.module_instance.target_type
            target_field = None

            if target_type == "tcp":
                target_field = "HOST"
            elif target_type == "http":
                target_field = "URL"

            target_filename = self.module_instance.options.get_option(target_field)

            try:
                target_file = open(target_filename, 'r')
                self.module_instance.targets = []
                for line in target_file.readlines():
                    self.module_instance.targets.append(line.strip())
                self.module_instance.multi_target = True
            except IOError as e:
                self._print_item(e, color=Fore.RED)
                return False

            targets = self.module_instance.targets
            targets_queue = Queue()
            for target in targets:
                targets_queue.put(target)

            if not targets_queue.empty():
                thread_count = int(self.module_instance.options.get_option("THREADS"))
                thread_queue = Queue(maxsize=thread_count)

                try:
                    while not targets_queue.empty():
                        while thread_queue.full():
                            time.sleep(0.1)

                        target = targets_queue.get()
                        thread_queue.put(1)
                        _thread = threading.Thread(target=self.check_thread,
                                                   args=(target, target_type, thread_queue))
                        _thread.start()

                    while not thread_queue.empty():
                        time.sleep(0.1)
                except KeyboardInterrupt:
                    self._print_item("Wait for existing process to exit...", color=Fore.RED)
                    while threading.activeCount() > 1:
                        time.sleep(0.5)
                    return None

            self.poutput("{style}[*]{style_end} module execution completed".format(
                style=Fore.BLUE + Style.BRIGHT,
                style_end=Style.RESET_ALL
            ))
            return None

        exploit_result = self.module_instance.check()

        if exploit_result is None:
            self._print_item("Check Error: check function no results returned")
            return None

        if exploit_result.status:
            self._print_item("Check success!")
            self._print_item(exploit_result.success_message)
        else:
            self._print_item("Exploit failure!", color=Fore.RED)
            self._print_item(exploit_result.error_message, color=Fore.RED)
        self.poutput("{style}[*]{style_end} module execution completed".format(
            style=Fore.BLUE + Style.BRIGHT,
            style_end=Style.RESET_ALL
        ))

    @with_category(CMD_DATABASE)
    def thgcmd_db_rebuild(self, args):
        """Rebuild database for search"""
        self.db_rebuild()
        self.poutput(style("Database rebuild done.", fg='GREEN'))

    @with_category(CMD_DATABASE)
    def thgcmd_reload(self, args):
        """reload the chose module"""
        self.thgcmd_use(self.module_name, module_reload=True)

    def set_prompt(self, module_type, module_name):
        module_prompt = " {module_type}({color}{module_name}{color_end})".format(
            module_type=module_type,
            module_name=module_name.replace(module_type + "/", ""),
            color=Fore.RED,
            color_end=Fore.GREEN
        )
        self.prompt = self.console_prompt + module_prompt + self.console_prompt_end
###################################################################################
###################################system##########################################
###################################################################################
    @with_category(CMD_SYSTEM)
    def thgcmd_battery(self,*args):
        """show battery status"""
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
    @with_category(CMD_SYSTEM)
    def thgcmd_who(self, *args):
        """
        A clone of 'who' command; print information about users who are
        currently logged in.
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
    @with_category(CMD_SYSTEM)
    def thgcmd_free(self,*args):
        """show memore info"""
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
    @with_category(CMD_SYSTEM)
    def thgcmd_sensors_temperatures(self,*args):
        """
        utility on Linux printing hardware temperatures.
        """
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
    @with_category(CMD_SYSTEM)
    def thgcmd_sensor(self,*args):

        """
        A clone of 'sensors' utility on Linux printing hardware temperatures,
        fans speed and battery info.
        """



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
    @with_category(CMD_SYSTEM)
    def thgcmd_fans(self,*args):
        """
        Show fans information.
        """

        import sys

        import psutil

        def main():
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
                print()


        main()
    @with_category(CMD_SYSTEM)
    def thgcmd_netstat(self,*args):
        # !/usr/bin/env python

        """
        A clone of 'netstat -antp' on Linux.
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
    @with_category(CMD_SYSTEM)
    def thgcmd_procsmensage(self,*args):
        """
        Show detailed memory usage about all (querable) processes.
        """

        import sys

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
    @with_category(CMD_SYSTEM)
    def thgcmd_pstree(self,*args):
        """
        Similar to 'ps aux --forest' on Linux, prints the process list
        as a tree structure.
        """
        import collections
        import sys

        import psutil

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

###################################################################################
###################################################################################
###################################################################################
    def _print_modules(self, modules, fields, title):
        self.poutput(style(title+ "\n", fg="cyan"))
        if(modules != [] and fields != []):
            self.poutput(style(tabulate(modules, headers=(fields), tablefmt='fancy_grid') + '\n', fg="Green"))
        else:
            self.poutput(style("No modules found!\n", fg="Green"))

    def _print_item(self, message, color=Fore.GREEN):
        self.poutput("{style}[+]{style_end} {message}".format(
            style=color + Style.BRIGHT,
            style_end=Style.RESET_ALL,
            message=message,
        ))
