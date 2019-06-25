"""
"Easteregg"
"""

from pwn import *

splash()

h = log.waitfor("You wrote", status="--")

while True:
    l = input('> ')
    h.status(l.upper())
