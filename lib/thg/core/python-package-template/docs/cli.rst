======================
Command Line Interface
======================

There are numerous tools in python to help you create a command line
interface. Some of these include ``click``, ``docopt``, and SO many
others. Personally I have found that ``argparse`` in the standard
library does 90% of the things that I need in a command line. Since
``argparse`` is in the stdlib full documentation is available `argparse
<https://docs.python.org/3/library/argparse.html>`_

--------
setup.py
--------

.. code-block:: python

   setup(
        ...
        entry_points={
             'console_scripts': [
                 '<command>=<package>.__main__:main'
             ]
         },
         ...
     )

---------------------
<package>/__main__.py
---------------------

.. code-block:: python

   import argparse
   import sys


   def main():
       parser = argparse.ArgumentParser()
       subparsers = parser.add_subparsers()
       add_subcommand_fizzbuzz(subparsers)
       if len(sys.argv) == 1:
           parser.print_help()
           sys.exit(1)
       args = parser.parse_args()
       args.func(args)


   def add_subcommand_fizzbuzz(subparsers):
       parser = subparsers.add_parser('fizzbuzz', help='do the fizzbuzz!')
       parser.set_defaults(func=handle_subcommand_fizzbuzz)
       parser.add_argument('-n', '--number', type=int, default=100, help='number for fizzbuzz to count to')


   def handle_subcommand_fizzbuzz(args):
       from pypkgtemp.hello import fizzbuzz
       fizzbuzz(args.number)


   if __name__ == '__main__':
       main()


And there you have the simplest non trivial and scalable
argparser. This demonstration shows how to create subcommands and take
options with certain types and defaults. You can run the example via
``<command> fizzbuzz -n 42`` or ``<command> fizzbuzz``.
