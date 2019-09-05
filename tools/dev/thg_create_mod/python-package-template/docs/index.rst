.. Python Package Template documentation master file, created by
   sphinx-quickstart on Fri Mar 30 08:47:11 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Python Package Template's documentation!
===================================================

This is an opinionated attempt to document how I deploy a python
application with documentation, testing, pypi, and continuous
deployment. This project will be updated as I change my python
development practices. Number one this is a learning experience.

This project is a python package itself and full documentation is
available on readthedocs. Each of the steps below includes a link to
the section in the documentation.

1. setup a bare python package with git repo (``setup.py``, ``README.md``, ``.gitignore``, ``<package>``)
2. setup pypi deployment with git tags ``vX.X.X``
3. setup conda deployment with git tags ``vX.X.X``
4. setup docker deployment with git tags ``vX.X.X``
5. setup testing on each commit with ``pytest``
6. setup documentation with ``sphinx`` on readthedocs and self hosted
7. setup command line interface with ``argparse``
8. setup badges for README.md

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   packaging
   pypi
   conda
   docker
   testing
   documentation
   cli
   badges

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
