# -*- coding: utf-8 -*-
import collections
import random
import re

from ..context import context, local_context
from ..log import getLogger
from ..util.fiddling import hexdump
from ..util.misc import force_bytes

log = getLogger(__name__)


class Encoder:
    _encoders = collections.defaultdict(lambda: [])

    #: Architecture which this encoder works on
    arch = None

    #: Blacklist of bytes which are known not to be supported
    blacklist = set()

    def __init__(self):
        """Shellcode encoder class

        Implements an architecture-specific shellcode encoder
        """
        Encoder._encoders[self.arch].append(self)

    def __call__(self, raw_bytes, avoid, pcreg):
        """avoid(raw_bytes, avoid)

        Arguments:
            raw_bytes(bytes):
                String of bytes to encode
            avoid(set):
                Set of bytes to avoid
            pcreg(str):
                Register which contains the address of the shellcode.
                May be necessary for some shellcode.
        """
        raise NotImplementedError()


@local_context
def encode(raw_bytes, avoid=None, expr=None, force=0, pcreg=''):
    """encode(raw_bytes, avoid, expr, force) -> bytes

    Encode shellcode ``raw_bytes`` such that it does not contain
    any bytes in ``avoid`` or ``expr``.

    Arguments:
        raw_bytes(bytes):  Sequence of shellcode bytes to encode.
        avoid(bytes):      Bytes to avoid
        expr(bytes, str):  Regular expression which matches bad characters.
        force(bool):       Force re-encoding of the shellcode, even if it
                           doesn't contain any bytes in ``avoid``.
    """
    orig_avoid = avoid
    avoid = set(avoid or b'')

    if expr:
        for byte in range(256):
            if re.search(force_bytes(expr), bytes([byte])):
                avoid.add(byte)

    if not (force or avoid & set(raw_bytes)):
        return raw_bytes

    encoders = Encoder._encoders[context.arch]
    random.shuffle(encoders)

    for encoder in encoders:
        if encoder.blacklist & avoid:
            continue

        try:
            v = encoder(raw_bytes, avoid, pcreg)
        except NotImplementedError:
            continue

        if avoid & set(v):
            log.warning_once("Encoder %s did not succeed" % encoder)
            continue

        return v

    avoid_errmsg = ''
    if orig_avoid and expr:
        avoid_errmsg = '%r and %r' % (orig_avoid, expr)
    elif expr:
        avoid_errmsg = repr(expr)
    else:
        avoid_errmsg = repr(bytes(avoid))

    args = (context.arch, avoid_errmsg, hexdump(raw_bytes))
    msg = "No encoders for %s which can avoid %s for\n%s" % args
    msg = msg.replace('%', '%%')
    log.error(msg)


re_alphanumeric = r'[^A-Za-z0-9]'
re_printable = r'[^\x21-\x7e]'
re_whitespace = r'\s'
re_null = r'\x00'
re_line = r'[\s\x00]'


@local_context
def null(raw_bytes, *args, **kwargs):
    """null(raw_bytes) -> bytes

    Encode the shellcode ``raw_bytes`` such that it does not
    contain any NULL bytes.

    Accepts the same arguments as :func:`encode`.
    """
    return encode(raw_bytes, expr=null, *args, **kwargs)


@local_context
def line(raw_bytes, *args, **kwargs):
    """line(raw_bytes) -> bytes

    Encode the shellcode ``raw_bytes`` such that it does not
    contain any NULL bytes or whitespace.

    Accepts the same arguments as :func:`encode`.
    """
    return encode(raw_bytes, expr=re_whitespace, *args, **kwargs)


@local_context
def alphanumeric(raw_bytes, *args, **kwargs):
    """alphanumeric(raw_bytes) -> bytes

    Encode the shellcode ``raw_bytes`` such that it does not
    contain any bytes except for [A-Za-z0-9].

    Accepts the same arguments as :func:`encode`.
    """
    return encode(raw_bytes, expr=re_alphanumeric, *args, **kwargs)


@local_context
def printable(raw_bytes, *args, **kwargs):
    """printable(raw_bytes) -> bytes

    Encode the shellcode ``raw_bytes`` such that it only contains
    non-space printable bytes.

    Accepts the same arguments as :func:`encode`.
    """
    return encode(raw_bytes, expr=re_printable, *args, **kwargs)


@local_context
def scramble(raw_bytes, *args, **kwargs):
    """scramble(raw_bytes) -> bytes

    Encodes the input data with a random encoder.

    Accepts the same arguments as :func:`encode`.
    """
    return encode(raw_bytes, force=1, *args, **kwargs)
