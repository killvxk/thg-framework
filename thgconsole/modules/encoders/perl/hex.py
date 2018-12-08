from thgconsole.core.ModulesBuild.Encoders.encoders import BaseEncoder
from thgconsole.core.ModulesBuild.Payloads.payloads import Architectures


class Encoder(BaseEncoder):
    __info__ = {
        "name": "Perl Hex Encoder",
        "description": "Module encodes PERL payload to Hex format.",
        "authors": (
            "Marcin Bury <marcin[at]threat9.com>",  # thg module
        ),
    }

    architecture = Architectures.PERL

    def encode(self, payload):
        encoded_payload = bytes(payload, "utf-8").hex()
        return "eval(pack('H*','{}'));".format(encoded_payload)
