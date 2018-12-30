from __future__ import absolute_import
from .auxiliares.cores.cores import *
# coding=utf-8
from .version.version import version

import importlib

version()
__thg_module__ = [
    'server',
    'version',
    'shells',
    'auxiliares',
    'anti_forensic',
    'crypto',
    'drone',
    'keylogger',
    'recon',
    'voip',
    'automation',
    'cryptography',
    'exploitation',
    'malware',
    'reversing',
    'automobile',
    'database',
    'fingerprint',
    'misc',
    'sniffer',
    'wireless',
    'auxiliares',
    'debugger',
    'firmware',
    'mobile',
    'social',
    'backdoor',
    'decompiler',
    'forensic',
    'networking',
    'spoff',
    'binary',
    'defensensive',
    'gpu',
    'os',
    'nfc',
    'nfc',
    'spoof',
    'version',
    'bluetooth',
    'defensive',
    'hardware',
    'packer',
    'stego',
    'code_audit',
    'disassembler',
    'honeypot',
    'proxy',
    'tunnel',
    'cracker',
    'dos',
    'ids',
    'radio',
    'unpacker',
    'auxiliares'
]
print("total modulos => " + str(len(__thg_module__)))

for module in __thg_module__:
    importlib.import_module('.%s' % module, 'thglibs')
'''
elif load == str(2):
    with open("load_libs")as fl:
        for i in fl.read().splitlines():
            extra_libs = []
            extra_libs.append(i)
            print(extra_libs)
            for module in extra_libs:
                importlib.import_module('.%s' % module, 'thglibs')

else:
    pass
'''
