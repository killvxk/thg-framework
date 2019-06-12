import socket
from lib.BaseMode.BaseMods import BaseExploit
import base64, binascii
from colorama import Fore
class Exploit(BaseExploit):
    def __init__(self):
        super(Exploit, self).__init__()
        self.update_info({
            "name": "encode",
            "description": "encode64",
            "author": ["test edit"],
            "references": [
                "base64 ",
            ],
            "disclosure_date": "2019-06-11",
            "service_name": "encode",
            "service_version": "all",
        })
        self.register_encode_target()
    def check(self):
        host = self.options.get_option("string")
        dsa = base64.b64encode(bytes(host, 'utf-8'))
        self.results.success(message="encode string =>{red} {host}".format(host=str(dsa)[2:-1],red=Fore.RED))
        return self.results

    def exploit(self):
        return self.check()
