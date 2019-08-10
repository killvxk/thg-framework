""" Utilities and helpers and etc. for plugins """

import importlib

from colorama import Fore
def load_plugin(THGBASECONSOLE, pluginName):
    """ Given the name of a plugin and a menu object, load it into the menu """
    # note the 'plugins' package so the loader can find our plugin
    fullPluginName = "plugins." + pluginName
    module = importlib.import_module(fullPluginName)
    pluginObj = module.Plugin(THGBASECONSOLE)
    THGBASECONSOLE.loadedPlugins[pluginName] = pluginObj

class Plugin():
    # to be overwritten by child
    description = "This is a description of this plugin."

    def __init__(self, THGBASECONSOLE):
        # having these multiple messages should be helpful for debugging
        # user-reported errors (can narrow down where they happen)
        print(Fore.RED+"[*] Initializing plugin...")
        # any future init stuff goes here

        print(Fore.RED+"[*] Doing custom initialization...")
        # do custom user stuff
        self.onLoad()

        # now that everything is loaded, register functions and etc. onto the main menu
        print(Fore.RED+"[*] Registering plugin with menu...")
        self.register(THGBASECONSOLE)

    def onLoad(self):
        """ Things to do during init: meant to be overridden by
        the inheriting plugin. """
        pass

    def register(self, THGBASECONSOLE):
        """ Any modifications made to the main menu are done here
        (meant to be overriden by child) """
        pass
