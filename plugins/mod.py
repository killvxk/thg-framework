""" An example of a plugin. """

#from lib.thg.base.plugins import Plugin
from colorama import Fore
from lib.thg.base.base import THGBASECONSOLE
from lib.thg.base.base import THGBASECONSOLE
from lib.thg.thgcmd import cmd2
# anything you simply write out (like a script) will run immediately when the
# module is imported (before the class is instantiated)

# this class MUST be named Plugin
class Plugin(cmd2.Cmd):
    def __init__(self, *args):
        super().__init__(*args)
        self.register_postparsing_hook(self.hookTestMethod)

    def hookTestMethod(self, params: cmd2.plugin.PostparsingData) -> cmd2.plugin.PostparsingData:
        print("Hello from your new plugin!")
        #self.poutput("before the loop begins")

    # description = "An example plugin."
    #
    # def onLoad(self):
    #     """ any custom loading behavior - called by init, so any
    #     behavior you'd normally put in __init__ goes here """
    #     print("Custom loading behavior happens now.")
    #
    #     # you can store data here that will persist until the plugin
    #     # is unloaded (i.e. Empire closes)
    #
    # def register(self, THGBASECONSOLE):
    #     """ any modifications to the mainMenu go here - e.g.
    #     registering functions to be run by user commands """
    #     print(help(THGBASECONSOLE.register_postcmd_hook))
    #     print(Fore.GREEN+"AAAAAAAAAAAAAAAAAAAA")
    #     THGBASECONSOLE.register_cmdfinalization_hook(self.thgcmd_test)
    #
    # def thgcmd_test(self, args):
    #     "An example of a plugin function."
    #     print("This is executed from a plugin!")
    #     print(Fore.RED+"[*] It can even import  functionality!")
    #
    #     # you can also store data in the plugin (see onLoad)
    #
    #     print("quase pronto =>{}".format(Fore.BLUE+"quase"))
