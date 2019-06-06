import socket
from lib.BaseMode.BaseMods import BaseExploit
import base64, binascii
from colorama import Fore
class Exploit(BaseExploit):
    def __init__(self):
        super(Exploit, self).__init__()
        self.update_info({
            "name": "redis unauthorized",
            "description": "redis unauthorized",
            "author": ["unknown"],
            "references": [
                "https://www.freebuf.com/column/158065.html",
            ],
            "disclosure_date": "2019-02-28",
            "service_name": "redis",
            "service_version": "*",
        })
        self.register_encode_target()
    def check(self):
        host = self.options.get_option("string")
        dsa = base64.b64encode(bytes(host, 'utf-8'))
        self.results.success(message="encode string =>{red} {host}".format(host=str(dsa)[2:-1],red=Fore.RED))
        return self.results

    def exploit(self):
        return self.check()