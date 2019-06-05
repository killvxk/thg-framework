#!/usr/bin/env python3
import argparse
import re
import sys

from pwnlib.util.fiddling import unhex

parser = argparse.ArgumentParser(description='''
Decodes hex-encoded data provided on the command line or via stdin.
''')
parser.add_argument('hex', nargs='*',
                    help='Hex bytes to decode')


def main():
    args = parser.parse_args()
    try:
        if not args.hex:
            s = sys.stdin.read()
            s = re.sub(r'\s', '', s)
            sys.stdout.buffer.write(unhex(s))
        else:
            sys.stdout.buffer.write(unhex(''.join(sys.argv[1:])))
    except TypeError as e:
        sys.stderr.write(str(e) + '\n')

if __name__ == '__main__':
    main()
