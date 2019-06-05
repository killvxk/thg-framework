#!/usr/bin/env python3
from argparse import ArgumentParser
from subprocess import CalledProcessError
from subprocess import check_output
from tempfile import NamedTemporaryFile

from pwn import *


def dump(objdump, elf):
    n = NamedTemporaryFile(delete=False)
    o = check_output([objdump, '-d', '-x', '-s', elf.path])
    n.write(o)
    n.flush()
    return n.name


def diff(a, b):
    try:
        output = check_output(['diff', a, b])
    except CalledProcessError as e:
        output = e.output

    return output.decode('utf8')


p = ArgumentParser()
p.add_argument('a')
p.add_argument('b')


def main():
    a = p.parse_args()

    with context.silent:
        x = ELF(a.a)
        y = ELF(a.b)

    if x.arch != y.arch:
        log.error("Architectures are not the same: %s vs %s" % (x.arch, y.arch))

    context.arch = x.arch

    objdump = pwnlib.asm.which_binutils('objdump')

    print(diff(dump(objdump, x), dump(objdump, y)))

if __name__ == '__main__':
    main()
