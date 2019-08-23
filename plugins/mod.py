""" An example of a plugin. """

#from lib.thg.base.plugins import Plugin
import argparse
from colorama import Fore
from lib.thg.base.base import THGBASECONSOLE
from lib.thg.thgcmd import cmd2, parsing, plugin
# anything you simply write out (like a script) will run immediately when the
# module is imported (before the class is instantiated)

# this class MUST be named Plugin
class Plugin(cmd2.Cmd):
    def __init__(self, *args, **kwargs):
        """Init"""
        super().__init__(*args, **kwargs)
        self.reset_counters()

    def reset_counters(self):
        """Reset hooks counters"""
        self.called_preparse = 0
        self.called_postparsing = 0
        self.called_precmd = 0
        self.called_postcmd = 0
        self.called_cmdfinalization = 0

    def thgcmd_say(self, msg):
        """Print the message"""
        self.poutput(msg)

    def help_say(self):
        """ help for say method"""
        print("Say help!")

    def hookTestMethod(self) -> None:
        self.poutput("before the loop begins")
        self.caju = 10
        # if not '|' in params.statement.raw:
        #     newinput = params.statement.raw + ' | less'
        #     params.statement = self.statement_parser.parse(newinput)
        # return params
    # def precmd(self, statement: cmd2.Statement) -> cmd2.Statement:
    #     """Override cmd.Cmd method"""
    #     self.called_precmd += 1
    #     return statement

    def precmd_hook(self, data: plugin.PrecommandData) -> plugin.PrecommandData:
        """A precommand hook"""
        self.called_precmd += 1
        return data

    # def thgcmd_say(self):
    #     """A help for this plugin"""

    def onLoad(self, line):
        """Load all hooks"""
        # self.hookTestMethod()
        self.register_preloop_hook(self.hookTestMethod)
        self.register_precmd_hook(self.precmd_hook)
        self.onecmd_plus_hooks('say mod loaded successfully')

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
