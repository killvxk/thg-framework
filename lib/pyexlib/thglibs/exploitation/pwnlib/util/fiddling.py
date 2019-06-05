# -*- coding: utf-8 -*-
import base64
import codecs
import random
import re
import string
import functools

from . import lists
from . import packing
from ..context import context
from ..log import getLogger
from ..term import text
from .cyclic import cyclic
from .misc import force_bytes

log = getLogger(__name__)


def unhex(s):
    """unhex(s) -> bytes

    Hex-decodes a bytes or string.

    Example:

        >>> unhex("74657374")
        b'test'
        >>> unhex("F\\n")
        b'\\x0f'
    """
    s = force_bytes(s)
    s = s.strip()
    if len(s) % 2 != 0:
        s = b'0' + s
    return codecs.decode(s, 'hex_codec')


def enhex(x):
    """enhex(x) -> str

    Hex-encodes a bytes or string.

    Example:

        >>> enhex("test")
        '74657374'
    """
    return codecs.encode(force_bytes(x), 'hex_codec').decode('utf8')


def urlencode(s):
    """urlencode(s) -> str

    URL-encodes a bytes or string.

    Example:

        >>> urlencode("test")
        '%74%65%73%74'
    """
    return ''.join(['%%%02x' % c for c in force_bytes(s)])


def urldecode(s, ignore_invalid=False):
    """urldecode(s, ignore_invalid=False) -> bytes

    URL-decodes a bytes or string.

    Example:

        >>> urldecode("test%20%41")
        b'test A'
        >>> urldecode("%qq")
        Traceback (most recent call last):
            ...
        ValueError: Invalid input to urldecode
        >>> urldecode("%qq", ignore_invalid=True)
        b'%qq'
    """
    s = force_bytes(s)
    res = []
    n = 0
    while n < len(s):
        if s[n] != ord('%'):
            res.append(s[n])
            n += 1
        else:
            cur = s[n + 1:n + 3]
            if re.match(b'[0-9a-fA-F]{2}', cur):
                res.append(int(cur, 16))
                n += 3
            elif ignore_invalid:
                res.append(ord('%'))
                n += 1
            else:
                raise ValueError("Invalid input to urldecode")

    return bytes(res)


def bits(s, endian='big', zero=0, one=1):
    """bits(s, endian='big', zero=0, one=1) -> list

    Converts the argument to a list of bits.

    Arguments:
        s(bytes, str, int): A string or number to be converted into bits.
        endian (str): The binary endian, default 'big'.
        zero: The representing a 0-bit.
        one: The representing a 1-bit.

    Returns:
        A list consisting of the values specified in `zero` and `one`.

    Examples:

        >>> bits(511, zero="+", one="-")
        ['+', '+', '+', '+', '+', '+', '+', '-', '-', '-', '-', '-', '-', '-', '-', '-']
        >>> sum(bits("test"))
        17
        >>> bits(0)
        [0, 0, 0, 0, 0, 0, 0, 0]
    """
    if endian not in ('little', 'big'):
        raise ValueError("bits(): 'endian' must be either 'little' or 'big'")
    else:
        little = endian == 'little'

    out = []
    if isinstance(s, (bytes, str)):
        s = force_bytes(s)
        for c in s:
            byte = []
            for _ in range(8):
                byte.append(one if c & 1 else zero)
                c >>= 1
            if little:
                out += byte
            else:
                out += byte[::-1]
    elif isinstance(s, int):
        if s == 0:
            out.append(zero)
        while s:
            bit, s = one if s & 1 else zero, s >> 1
            out.append(bit)
        while len(out) % 8:
            out.append(zero)
        if not little:
            out = out[::-1]
    else:
        raise ValueError("bits(): 's' must be either a string or a number")

    return out


def bits_str(s, endian='big', zero='0', one='1'):
    """bits_str(s, endian='big', zero='0', one='1') -> str

    A wrapper around :func:`bits`, which converts the output into a string.

    Examples:

        >>> bits_str(511)
        '0000000111111111'
        >>> bits_str("bits_str", endian="little")
        '0100011010010110001011101100111011111010110011100010111001001110'
    """
    return ''.join(bits(s, endian, zero, one))


def unbits(s, endian='big'):
    """unbits(s, endian='big') -> bytes

    Converts an iterable of bits into a string.

    Arguments:
        s: Iterable of bits
        endian (str):  The string "little" or "big", which specifies the bits endianness.

    Returns:
        A string of the decoded bits.

    Example:
        >>> unbits([1])
        b'\\x80'
        >>> unbits([1], endian='little')
        b'\\x01'
        >>> unbits(bits('hello'), endian='little')
        b'\\x16\\xa666\\xf6'
    """
    if endian == 'little':
        u = lambda s: int(s[::-1], 2)
    elif endian == 'big':
        u = lambda s: int(s, 2)
    else:
        raise ValueError("unbits(): 'endian' must be either 'little' or 'big'")

    out = []
    cur = ''

    for c in s:
        if c in ('1', 1, True):
            cur += '1'
        elif c in ('0', 0, False):
            cur += '0'
        else:
            raise ValueError("unbits(): cannot decode the value %r into a bit" % c)

        if len(cur) == 8:
            out.append(u(cur))
            cur = ''
    if cur:
        out.append(u(cur.ljust(8, '0')))

    return bytes(out)


def bitswap(s):
    """bitswap(s) -> bytes

    Reverses the bits in every byte of a given string.

    Example:
        >>> bitswap("1234")
        b'\\x8cL\\xcc,'
    """
    out = []

    for c in s:
        out.append(unbits(bits_str(c)[::-1]))

    return b''.join(out)


def bitswap_int(n, width):
    """bitswap_int(n) -> int

    Reverses the bits of a numbers and returns the result as a new number.

    Arguments:
        n (int): The number to swap.
        width (int): The width of the integer

    Examples:
        >>> hex(bitswap_int(0x1234, 8))
        '0x2c'
        >>> hex(bitswap_int(0x1234, 16))
        '0x2c48'
        >>> hex(bitswap_int(0x1234, 24))
        '0x2c4800'
        >>> hex(bitswap_int(0x1234, 25))
        '0x589000'
    """
    # Make n fit inside the width
    n &= (1 << width) - 1

    # Convert into bits
    s = bits_str(n, endian='little').ljust(width, '0')[:width]

    # Convert back
    return int(s, 2)


def b64e(s):
    """b64e(s) -> str

    Base64 encodes a bytes or string

    Example:

        >>> b64e("test")
        'dGVzdA=='
    """
    return base64.b64encode(force_bytes(s)).decode('utf8')


def b64d(s):
    """b64d(s) -> bytes

    Base64 decodes a bytes or string

    Example:

        >>> b64d('dGVzdA==')
        b'test'
    """
    return base64.b64decode(force_bytes(s))


# misc binary functions
def xor(*args, **kwargs):
    """xor(*args, cut='max') -> bytes

    Flattens its arguments using :func:`pwnlib.util.packing.flat` and
    then xors them together. If the end of a string is reached, it wraps
    around in the string.

    Arguments:
        args: The arguments to be xor'ed together.
        cut: How long a string should be returned.
             Can be either 'min'/'max'/'left'/'right' or a number.

    Returns:
        The string of the arguments xor'ed together.

    Example:
        >>> xor('lol', 'hello', 42)
        b'. ***'
    """
    cut = kwargs.pop('cut', 'max')

    if kwargs != {}:
        raise TypeError("xor() got an unexpected keyword argument '%s'" % kwargs.pop()[0])

    if len(args) == 0:
        raise ValueError("Must have something to xor")

    strs = [packing.flat(s, word_size=8, sign=False, endianness='little') for s in args]
    strs = [s for s in strs if s != b'']

    if strs == []:
        return b''

    if isinstance(cut, int):
        cut = cut
    elif cut == 'left':
        cut = len(strs[0])
    elif cut == 'right':
        cut = len(strs[-1])
    elif cut == 'min':
        cut = min(len(s) for s in strs)
    elif cut == 'max':
        cut = max(len(s) for s in strs)
    else:
        raise ValueError("Not a valid argument for 'cut'")

    def get(n):
        return functools.reduce(lambda x, y: x ^ y, [s[n % len(s)] for s in strs])

    return bytes([get(n) for n in range(cut)])


def xor_pair(data, avoid=b'\x00\n'):
    """xor_pair(data, avoid=b'\\x00\\n') -> None or (bytes, bytes)

    Finds two strings that will xor into a given string, while only
    using a given alphabet.

    Arguments:
        data (bytes, str): The desired string.
        avoid (bytes, str): The list of disallowed characters. Defaults to nulls and newlines.

    Returns:
        Two strings which will xor to the given string. If no such two strings exist, then None is returned.

    Example:

        >>> xor_pair("test")
        (b'\\x01\\x01\\x01\\x01', b'udru')
    """
    if isinstance(data, int):
        data = packing.pack(data)

    data = force_bytes(data)
    avoid = force_bytes(avoid)
    alphabet = [n for n in range(256) if n not in avoid]

    res1 = []
    res2 = []

    for c1 in data:
        if context.randomize:
            random.shuffle(alphabet)

        for c2 in alphabet:
            c3 = c1 ^ c2
            if c3 in alphabet:
                res1.append(c2)
                res2.append(c3)
                break
        else:
            return None

    return bytes(res1), bytes(res2)


def xor_key(data, avoid=b'\x00\n', size=None):
    r"""xor_key(data, avoid='\x00\n', size=None) -> None or (bytes, bytes)

    Finds a ``size``-width value that can be XORed with a string
    to produce ``data``, while neither the XOR value or XOR string
    contain any bytes in ``avoid``.

    Arguments:
        data (bytes, str): The desired string.
        avoid (bytes, str): The list of disallowed characters. Defaults to nulls and newlines.
        size (int): Size of the desired output value, default is word size.

    Returns:
        A tuple containing two strings; the XOR key and the XOR string.
        If no such pair exists, None is returned.

    Example:

        >>> xor_key("Hello, world")
        (b'\x01\x01\x01\x01', b'Idmmn-!vnsme')
    """
    data = force_bytes(data)
    avoid = force_bytes(avoid)
    size = size or context.bytes
    alphabet = [n for n in range(256) if n not in avoid]

    if len(data) % size:
        log.error("Data must be padded to size for xor_key")

    words = lists.group(size, data)
    columns = [b''] * size
    for word in words:
        for i, byte in enumerate(word):
            columns[i] += bytes([byte])

    result = []

    for column in columns:
        if context.randomize:
            random.shuffle(alphabet)

        for c2 in alphabet:
            if all(c ^ c2 in alphabet for c in column):
                result.append(c2)
                break
        else:
            return None

    return bytes(result), xor(data, result)


def randoms(count, alphabet=string.ascii_lowercase):
    """randoms(count, alphabet=string.ascii_lowercase) -> str

    Returns a random string of a given length using only the specified alphabet.

    Arguments:
        count (int): The length of the desired string.
        alphabet (str): The alphabet of allowed characters. Defaults to all lowercase characters.

    Returns:
        A random string.

    Example:

        >>> randoms(10) #doctest: +SKIP
        'evafjilupm'
        >>> randoms(10, alphabet=b'abcdef') #doctest: +SKIP
        b'dcacbfccdc'
    """
    if isinstance(alphabet, str):
        return ''.join(random.choice(alphabet) for _ in range(count))
    elif isinstance(alphabet, bytes):
        return bytes(random.choice(alphabet) for _ in range(count))


def rol(n, k, word_size=None):
    """Returns a rotation by `k` of `n`.

    When `n` is a number, then means ``((n << k) | (n >> (word_size - k)))`` truncated to `word_size` bits.

    When `n` is a list, tuple or string, this is ``n[k % len(n):] + n[:k % len(n)]``.

    Arguments:
        n: The value to rotate.
        k(int): The rotation amount. Can be a positive or negative number.
        word_size(int): If `n` is a number, then this is the assumed bitsize of `n`.  Defaults to :data:`pwnlib.context.word_size` if `None` .

    Example:

        >>> rol('abcdefg', 2)
        'cdefgab'
        >>> rol('abcdefg', -2)
        'fgabcde'
        >>> hex(rol(0x86, 3, 8))
        '0x34'
        >>> hex(rol(0x86, -3, 8))
        '0xd0'
    """
    word_size = word_size or context.word_size

    if not isinstance(word_size, int) or word_size <= 0:
        raise ValueError("rol(): 'word_size' must be a strictly positive integer")

    if not isinstance(k, int):
        raise ValueError("rol(): 'k' must be an integer")

    if isinstance(n, (bytes, str, list, tuple)):
        return n[k % len(n):] + n[:k % len(n)]
    elif isinstance(n, int):
        k = k % word_size
        n = (n << k) | (n >> (word_size - k))
        n &= (1 << word_size) - 1

        return n
    else:
        raise ValueError("rol(): 'n' must be an integer, string, list or tuple")


def ror(n, k, word_size=None):
    """A simple wrapper around :func:`rol`, which negates the values of `k`."""
    return rol(n, -k, word_size)


def naf(n):
    """naf(int) -> int generator

    Returns a generator for the non-adjacent form (NAF[1]) of a number, `n`.  If
    `naf(n)` generates `z_0, z_1, ...`, then `n == z_0 + z_1 * 2 + z_2 * 2**2,
    ...`.

    [1] https://en.wikipedia.org/wiki/Non-adjacent_form

    Example:

        >>> n = 45
        >>> m = 0
        >>> x = 1
        >>> for z in naf(n):
        ...     m += x * z
        ...     x *= 2
        >>> n == m
        True
    """
    while n:
        z = 2 - n % 4 if n & 1 else 0
        n = (n - z) // 2
        yield z


def isprint(s):
    """isprint(s) -> bool

    Return True if the argument is printable

    Example:

        >>> isprint(ord('a'))
        True
        >>> isprint('abc')
        True
        >>> isprint('\x01')
        False
        >>> isprint(b'abc')
        True
        >>> isprint(b'\x01')
        False
    """
    chars = string.ascii_letters + string.digits + string.punctuation + ' '

    if isinstance(s, int):
        return chr(s) in chars
    elif isinstance(s, bytes):
        return all(c in map(ord, chars) for c in s)
    else:
        return all(c in chars for c in s)


def hexii(s, width=16, skip=True):
    """hexii(s, width=16, skip=True) -> str

    Return a HEXII-dump of a string.

    Arguments:
        s(str): The string to dump
        width(int): The number of characters per line
        skip(bool): Should repeated lines be replaced by a "*"

    Returns:
        A HEXII-dump in the form of a string.
    """
    return hexdump(s, width, skip, True)


def _hexiichar(c):
    HEXII = string.punctuation + string.digits + string.ascii_letters

    if c in map(ord, HEXII):
        return ".%c " % c
    elif c == 0:
        return "   "
    elif c == 0xff:
        return "## "
    else:
        return "%02x " % c

default_style = {
    'marker': text.gray if text.has_gray else text.blue,
    'nonprintable': text.gray if text.has_gray else text.blue,
    'highlight': text.white_on_red,
    '00': text.red,
    'ff': text.green,
}

cyclic_pregen = ''


def sequential_lines(a, b):
    return (a + b) in cyclic_pregen


def update_cyclic_pregenerated(size):
    global cyclic_pregen
    cyclic_pregen = cyclic(size)


def hexdump_iter(s, width=16, skip=True, hexii=False, begin=0,
                 style=None, highlight=None, cyclic=False):
    """hexdump_iter(s, width=16, skip=True, hexii=False, begin=0,
                    style=None, highlight=None, cyclic=False) -> str generator

    Return a hexdump-dump of a string as a generator of lines.

    Arguments:
        s(str): The string to dump
        width(int): The number of characters per line
        skip(bool): Set to True, if repeated lines should be replaced by a "*"
        hexii(bool): Set to True, if a hexii-dump should be returned instead of a hexdump.
        begin(int):  Offset of the first byte to print in the left column
        style(dict): Color scheme to use.
        highlight(iterable): Byte values to highlight.
        cyclic(bool): Attempt to skip consecutive, unmodified cyclic lines

    Returns:
        A hexdump-dump in the form of a string.
    """
    style = style or {}
    highlight = highlight or []

    for b in highlight:
        if isinstance(b, (bytes, str)):
            b = ord(b)
        style['%02x' % b] = text.white_on_red
    _style = style
    style = default_style.copy()
    style.update(_style)

    skipping = False
    last_unique = ''
    byte_width = len('00 ')
    column_sep = '  '
    line_fmt = '%%(offset)08x  %%(hexbytes)-%is │%%(printable)s│' % (len(column_sep) +
                                                                     (width * byte_width))
    spacer = ' '
    marker = (style.get('marker') or (lambda s: s))('│')

    if hexii:
        column_sep = ''
        line_fmt = '%%(offset)08x  %%(hexbytes)-%is│' % (len(column_sep) +
                                                         (width * byte_width))
    else:
        def style_byte(b):
            hbyte = '%02x' % b
            abyte = chr(b) if isprint(b) else '·'
            if hbyte in style:
                st = style[hbyte]
            elif isprint(b):
                st = style.get('printable')
            else:
                st = style.get('nonprintable')
            if st:
                hbyte = st(hbyte)
                abyte = st(abyte)
            return hbyte, abyte

        cache = [style_byte(b) for b in range(256)]

    if cyclic:
        update_cyclic_pregenerated(len(s))

    chunks = lists.group(width, s)

    for line, chunk in enumerate(chunks):
        # If this chunk is the same as the last unique chunk,
        # use a '*' instead.
        if line != 0 \
                and line != len(chunks) - 1 \
                and skip \
                and (last_unique == chunk or (cyclic and sequential_lines(last_unique, chunk))):
            last_unique = chunk
            if not skipping:
                yield '*'
                skipping = True
            continue

        # Chunk is unique, save for next iteration
        last_unique = chunk
        skipping = False

        # Cenerate contents for line
        offset = begin + line * width
        hexbytes = ''
        printable = ''
        for i, b in enumerate(chunk):
            if not hexii:
                hbyte, abyte = cache[b]
            else:
                hbyte, abyte = _hexiichar(b), ''

            if i % 4 == 3 and i < width - 1:
                hbyte += spacer
                abyte += marker

            hexbytes += hbyte + ' '
            printable += abyte

        if i + 1 < width:
            delta = width - i - 1
            hexbytes += ' ' * (byte_width * delta + (delta - 1) // 4)

        line = line_fmt % {'offset': offset, 'hexbytes': hexbytes, 'printable': printable}
        yield line

    line = "%08x" % (len(s) + begin)
    yield line


def hexdump(s, width=16, skip=True, hexii=False, begin=0,
            style=None, highlight=None, cyclic=False):
    """hexdump(s, width=16, skip=True, hexii=False, begin=0,
               style=None, highlight=None, cyclic=False) -> str generator

    Arguments:

        s(str, bytes): The data to hexdump.
        width(int): The number of characters per line
        skip(bool): Set to True, if repeated lines should be replaced by a "*"
        hexii(bool): Set to True, if a hexii-dump should be returned instead
                     of a hexdump.
        begin(int): Offset of the first byte to print in the left column
        style(dict): Color scheme to use.
        highlight(iterable): Byte sequences to highlight.  A byte sequence
                             is an iterable where each element is either a
                             character or an integer, or `None` which means
                             "any byte".  Output lines containing a match will
                             have a "<" appended (hint: grep for "<$").
    """
    s = packing.flat(s)
    return '\n'.join(hexdump_iter(s,
                                  width,
                                  skip,
                                  hexii,
                                  begin,
                                  style,
                                  highlight,
                                  cyclic))


def negate(value, width=None):
    """
    Returns the two's complement of 'value'.
    """
    if width is None:
        width = context.bits
    mask = ((1 << width) - 1)
    return ((mask + 1) - value) & mask


def bnot(value, width=None):
    """
    Returns the binary inverse of 'value'.
    """
    if width is None:
        width = context.bits
    mask = ((1 << width) - 1)
    return mask ^ value
