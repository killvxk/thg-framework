import random
import string

from . import builder
from ...encoder import Encoder
from ....context import context


class ArmEncoder(Encoder):
    r"""Generates an alphanumeric decoder for ARM.

    Example:

        >>> context.clear(arch='arm')
        >>> shellcode = asm(shellcraft.sh())
        >>> encoded = pwnlib.encoders.arm.alphanumeric.encode(shellcode, b'')
        >>> p = run_shellcode(encoded)
        >>> p.sendline('echo hello; exit')
        >>> p.recvline()
        b'hello\n'
    """

    arch = 'arm'
    blacklist = {c for c in range(256) if chr(c) in string.ascii_letters + string.digits}

    def __call__(self, raw_bytes, avoid, pcreg=None):
        icache_flush = 1

        # If randomization is disabled, ensure that the seed
        # is always the same for the builder.
        state = random.getstate()
        if not context.randomize:
            random.seed(1)

        try:
            b = builder.builder()

            enc_data = b.enc_data_builder(raw_bytes)
            dec_loop = b.DecoderLoopBuilder(icache_flush)
            enc_dec_loop = b.encDecoderLoopBuilder(dec_loop)
            dec = b.DecoderBuilder(dec_loop, icache_flush)

            output, dec = b.buildInit(dec)

            output += dec
            output += enc_dec_loop
            output += enc_data
        finally:
            random.setstate(state)

        return output


class ThumbEncoder(ArmEncoder):
    arch = 'thumb'

encode = ArmEncoder()
