#!/usr/bin/env python3
import argparse

from pwn import *

from . import common

parser = argparse.ArgumentParser(
    description='Check binary security settings'
)

parser.add_argument(
    'elf',
    nargs='+',
    type=argparse.FileType('rb'),
    help='Files to check'
)


def main():
    args = parser.parse_args()
    for f in args.elf:
        e = ELF(f.name)

if __name__ == '__main__':
    main()
