""" An example of a plugin. """

#from lib.thg.base.plugins import Plugin
import argparse
from colorama import Fore
from lib.thg.base.base import THGBASECONSOLE
from lib.thg.thgcmd.cmd2 import with_category
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

    @with_category("template")
    def thgcmd_template(self, msg):
        """Print the message"""
        self.poutput(msg)


    def help_say(self):
        """ help for say method"""
        print("Say help!")

    def hookTestMethod(self) -> None:
        self.poutput("before the loop begins")
        self.caju = 10

    def precmd_hook(self, data: plugin.PrecommandData) -> plugin.PrecommandData:
        """A precommand hook"""
        self.called_precmd += 1
        return data

    def onLoad(self, line):
        """Load all hooks"""
        # self.hookTestMethod()
        self.register_preloop_hook(self.hookTestMethod)
        self.register_precmd_hook(self.precmd_hook)
        self.onecmd_plus_hooks('say mod loaded successfully')
