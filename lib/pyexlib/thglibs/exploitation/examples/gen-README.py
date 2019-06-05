#!/usr/bin/env python3
"""
Script to generate README.md
"""

from pwn import *


out = '''# Examples
While these examples should all work, they are not very representative of
the pwntools project.

We have a plan to create a separate repository with examples, primarily
exploits. Until we do so, we recommend new users to look at
https://python3-pwntools.readthedocs.org, as this is a better overview of our
features.

In no particular order the docstrings for each example:

'''

for dirpath, dirnames, filenames in os.walk('.'):
    for filename in sorted(filenames):
        if not (filename.endswith('.py') and filename != __file__):
            continue
        path = os.path.join(dirpath, filename)[2:]  # strip './'
        log.info('-> %s' % path)
        data = read(path).strip()
        if data[0:3] not in ('"""', "'''"):
            log.warning('  Has no docstring!')
            continue
        try:
            i = data.index(data[0:3], 3)
        except ValueError:
            log.warning('  Docstring is weird')
            continue
        doc = util.safeeval.const(data[0:i + 3])
        out += '* `%s`\n' % path
        out += '```%s```\n' % doc

write('README.md', out)
