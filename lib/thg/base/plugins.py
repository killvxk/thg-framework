""" Utilities and helpers and etc. for plugins """

import importlib
from lib.thg.thgcmd import cmd2

COMMAND_FUNC_PREFIX = 'thgcmd_'
HELP_FUNC_PREFIX = 'help_'

from colorama import Fore
def load_plugin(THGBASECONSOLE, pluginName, line, statement):
    """ Given the name of a plugin and a menu object, load it into the menu """
    # note the 'plugins' package so the loader can find our plugin
    fullPluginName = "plugins." + pluginName
    module = importlib.import_module(fullPluginName)
    st = cmd2.StatementParser.parse(statement, line)
    pluginObj = module.Plugin(THGBASECONSOLE, cmd2.StatementParser)
    THGBASECONSOLE.loadedPlugins = {str(pluginName): pluginObj}
    pluginObj.onLoad(line)
    thgcmd_say = getattr(pluginObj, "thgcmd_say")

    # return [name[len(COMMAND_FUNC_PREFIX):] for name in plugin_funcs
    return [thgcmd_say,"thgcmd_say"]


class Plugin():
    # to be overwritten by child
    description = "This is a description of this plugin."

    def __init__(self, THGBASECONSOLE):
        """Init"""
        # having these multiple messages should be helpful for debugging
        # user-reported errors (can narrow down where they happen)
        print(Fore.RED+"[*] Initializing plugin...")
        # any future init stuff goes here

        print(Fore.RED+"[*] Doing custom initialization...")
        # do custom user stuff
        self.onLoad(self)

        # now that everything is loaded, register functions and etc. onto the main menu
        print(Fore.RED+"[*] Registering plugin with menu...")
        self.register(THGBASECONSOLE)

    def onLoad(self):
        """ Things to do during init: meant to be overridden by
        the inheriting plugin. """
        print("Onload")
        pass

    def register(self, THGBASECONSOLE):
        """ Any modifications made to the main menu are done here
        (meant to be overriden by child) """
        pass
