Installation
============

python3-pwntools is best supported on Ubuntu 12.04 and 14.04, but most
functionality should work on any Posix-like distribution (Debian, Arch,
FreeBSD, OSX, etc.).

Prerequisites
-------------

In order to get the most out of ``pwntools``, you should have the
following system libraries installed.

.. toctree::
   :maxdepth: 3
   :glob:

   install/*

Released Version
-----------------

pwntools is available as a ``pip`` package.

.. code-block:: bash

    $ apt-get update
    $ apt-get install python3 python3-dev python3-pip git
    $ pip3 install --upgrade git+https://github.com/arthaud/python3-pwntools.git

Latest Version
--------------

Alternatively if you prefer to use the latest version from the
repository:

.. code-block:: bash

    $ git clone https://github.com/arthaud/python3-pwntools
    $ cd python3-pwntools
    $ pip3 install -e .

.. _Ubuntu: https://launchpad.net/~pwntools/+archive/ubuntu/binutils
