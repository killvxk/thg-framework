#!/usr/bin/env python3
import argparse
import sys

from pwnlib.util.fiddling import enhex

parser = argparse.ArgumentParser(description='''
Hex-encodes data provided on the command line or via stdin.
''')
parser.add_argument('data', nargs='*',
                    help='Data to convert into hex')


def main():
    args = parser.parse_args()
    if not args.data:
        print(enhex(sys.stdin.read()))
    else:
        print(enhex(' '.join(args.data)))

if __name__ == '__main__':
    main()
