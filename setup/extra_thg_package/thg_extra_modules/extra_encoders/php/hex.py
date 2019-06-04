from binascii import hexlify
from thgconsole.core.ModulesBuild.Encoders.encoders import BaseEncoder
from thgconsole.core.ModulesBuild.Payloads.payloads import Architectures


class Encoder(BaseEncoder):
    __info__ = {
        "name": "PHP Hex Encoder",
        "description": "Module encodes PHP payload to Hex format.",
        "authors": (
            "Marcin Bury <marcin[at]threat9.com>",  # thg module
        ),
    }

    architecture = Architectures.PHP

    def encode(self, payload):
        encoded_payload = str(hexlify(bytes(payload, "utf-8")), "utf-8")
        return "eval(hex2bin('{}'));".format(encoded_payload)
