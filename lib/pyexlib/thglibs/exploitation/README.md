![pwntools logo](docs/source/logo.png?raw=true)

[![Docs latest](https://readthedocs.org/projects/python3-pwntools/badge/?version=latest)](https://python3-pwntools.readthedocs.org/en/latest/)
[![Travis](https://travis-ci.org/arthaud/python3-pwntools.svg?branch=master)](https://travis-ci.org/arthaud/python3-pwntools)
[![Twitter](https://img.shields.io/badge/twitter-Gallopsled-4099FF.svg?style=flat)](https://twitter.com/Gallopsled)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)

Unofficial fork for python 3 of pwntools, the CTF framework and exploit development library. It is designed for rapid prototyping and development, and intended to make exploit writing as simple as possible.

**This project is not maintained anymore.**

```python
from pwn import *
context(arch='i386', os='linux')

r = remote('exploitme.example.com', 31337)
# EXPLOIT CODE GOES HERE
r.send(asm(shellcraft.sh()))
r.interactive()
```

# Origin

python3-pwntools is a fork of the [`pwntools`](https://github.com/Gallopsled/pwntools) project.  I also merged [`binjitsu`](https://github.com/binjitsu/binjitsu) into it so you can enjoy all the features of that great fork!

# Documentation

Our documentation is available at [python3-pwntools.readthedocs.org](https://python3-pwntools.readthedocs.org/en/latest/)

To get you started, we've provided some example solutions for past CTF challenges in our [write-ups repository](https://github.com/binjitsu/examples).

# Installation

python3-pwntools is best supported on 64-bit Ubuntu 12.04 and 14.04, but most functionality should work on any Posix-like distribution (Debian, Arch, FreeBSD, OSX, etc.). Python 3.2 to 3.5 are supported.

Most of the functionality of python3-pwntools is self-contained and Python-only.  You should be able to get running quickly with

```sh
apt-get update
apt-get install python3 python3-dev python3-pip git
pip3 install --upgrade git+https://github.com/arthaud/python3-pwntools.git
```

However, some of the features (assembling/disassembling foreign architectures) require non-Python dependencies.  For more information, see the [complete installation instructions here](https://python3-pwntools.readthedocs.org/en/latest/install.html).

# Contribution

See [CONTRIBUTING.md](CONTRIBUTING.md)

# Contact

If you have any questions not worthy of a [bug report](https://github.com/arthaud/python3-pwntools/issues), feel free to ping
at [`Maxima` on Freenode](irc://irc.freenode.net/pwntools) and ask away.
Click [here](https://kiwiirc.com/client/irc.freenode.net/pwntools) to connect.
