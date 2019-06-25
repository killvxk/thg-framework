import argparse
import sys

from pwn import *

from . import common

parser = argparse.ArgumentParser(
    description='Shellcode encoder'
)


parser.add_argument(
    "-f", "--format",
    help="Output format (defaults to hex for ttys, otherwise raw)",
    choices=['raw', 'hex', 'string', 'elf']
)

parser.add_argument(
    "-o", "--output",
    metavar='file',
    help="Output file (defaults to stdout)",
    type=argparse.FileType('w'),
    default=sys.stdout
)

parser.add_argument(
    '-c', '--context',
    metavar='context',
    action='append',
    type=common.context_arg,
    choices=common.choices,
    help='The os/architecture/endianness/bits the shellcode will run in (default: linux/i386), choose from: %s' % common.choices,
)

parser.add_argument(
    '-p', '--alphanumeric',
    action='store_true',
    help='Encode the shellcode with an alphanumeric encoder'
)

parser.add_argument(
    '-v', '--avoid',
    action='append',
    help='Encode the shellcode to avoid the listed bytes'
)

parser.add_argument(
    '-n', '--newline',
    dest='avoid',
    action='append_const',
    const='0a',
    help='Encode the shellcode to avoid newlines'
)

parser.add_argument(
    '-z', '--zero',
    dest='avoid',
    action='append_const',
    const='00',
    help='Encode the shellcode to avoid NULL bytes'
)

parser.add_argument(
    '-d',
    '--debug',
    help='Debug the shellcode with GDB',
    action='store_true'
)


def main():
    args = parser.parse_args()
    tty = args.output.isatty()

    if sys.stdin.isatty():
        parser.print_usage()
        sys.exit(0)

    data = sys.stdin.buffer.read()
    output = data
    fmt = args.format or ('hex' if tty else 'raw')
    formatters = {
        'r': bytes,
        'h': enhex,
        's': lambda d: repr(d)[1:]
    }

    if args.alphanumeric:
        output = alphanumeric(output)

    if args.avoid:
        avoid = unhex(''.join(args.avoid))
        output = encode(output, avoid)

    if args.debug:
        proc = gdb.debug_shellcode(output, arch=context.arch)
        proc.interactive()
        sys.exit(0)

    if fmt[0] == 'e':
        args.output.write(make_elf(output))
        try:
            os.fchmod(args.output.fileno(), 0o700)
        except OSError:
            pass
    else:
        output = formatters[fmt[0]](output)
        args.output.write(force_bytes(output))

    if tty and fmt is not 'raw':
        args.output.write(b'\n')

if __name__ == '__main__':
    main()
