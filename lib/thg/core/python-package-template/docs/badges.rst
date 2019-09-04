======
Badges
======

Obviously the most important part about creating packages is the
amount of flair that you have. Badges are the way to achieve
this. Many of the sites described in the documentation provide badges
such as conda, gitlab, and readthedocs. Sadly PyPi does not provide
badges but we can still get them from `shields.io
<https://shields.io>`_.

For the conda badges go to
``anaconda.org/<username>/<package>/badges`` and you will see a list
of available badges that you can use. For gitlab badges go to
``https://gitlab.com/<username>/<project>/settings/ci_cd``
and scroll to Pipeline status pipeline status and coverage report
should be available. The coverage report relies on the fact that you
setup coverage described in the testing section. For readthedocs a single badge is provided to show that documentation is building ``http://<package>.readthedocs.io/en/latest/?badge=latest``.

Markdown and restructured text are not the best formats for creating
tables (`org mode is <https://orgmode.org/manual/Tables.html>`_). But
for non emacs uses and a way to embed a table in markdown we can just
use HTML. I stole this idea from what the `pandas developers did
<https://raw.githubusercontent.com/pandas-dev/pandas/master/README.md>`_.

They use a simple html table.

.. code-block:: html

   <table>
   <tr>
     <td>Latest Release</td>
     <td><img src="https://img.shields.io/pypi/v/pypkgtemp.svg" alt="latest release" /></td>
   </tr>
     <td></td>
     <td><img src="https://anaconda.org/costrouc/pypkgtemp/badges/version.svg" alt="latest release" /></td>
   </tr>
   <tr>
     <td>Package Status</td>
     <td><img src="https://img.shields.io/pypi/status/pypkgtemp.svg" alt="status" /></td>
   </tr>
   <tr>
     <td>License</td>
     <td><img src="https://img.shields.io/pypi/l/pypkgtemp.svg" alt="license" /></td>
   </tr>
   <tr>
     <td>Build Status</td>
     <td>
       <a href="https://gitlab.com/costrouc/python-package-template/pipelines">
       <img src="https://gitlab.com/costrouc/python-package-template/badges/master/pipeline.svg" alt="gitlab pipeline status" />
       </a>
     </td>
   </tr>
   <tr>
     <td>Coverage</td>
     <td><img src="https://gitlab.com/costrouc/python-package-template/badges/master/coverage.svg" alt="coverage" /></td>
   </tr>
   <tr>
     <td>Conda</td>
     <td>
       <a href="https://gitlab.com/costrouc/python-package-template">
       <img src="https://anaconda.org/costrouc/pypkgtemp/badges/downloads.svg" alt="conda downloads" />
       </a>
     </td>
   </tr>
   <tr>
     <td>Documentation</td>
     <td>
       <a href="https://costrouc-python-package-template.readthedocs.io/en/latest/">
       <img src="http://costrouc-python-package-template.readthedocs.io/en/latest/?badge=latest" alt="readthedocs documentation" />
       </a>
     </td>
   </tr>
   </table>

Looking at a ``README.md`` you can see the resulting table.

Gitlab Badges
-------------

As of April 20th 2018, Gitlab supports badges that do not need to be
in the ``README.md``. This is honestly much cleaner. In your project
repository go to ``settings->badges`` and add each badge.
