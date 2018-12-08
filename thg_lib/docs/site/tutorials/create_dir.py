import os
import glob

__thg_module__ = [
    'server',
    'version',
    'shells',
    'thg_docs',
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
    'thg_windows',
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
for i in __thg_module__:
    try:
        os.system("touch " + i + ".md")

    except FileExistsError:
        print(i + " pass")

'''
 
'''
