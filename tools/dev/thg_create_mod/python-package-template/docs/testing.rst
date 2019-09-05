Testing
=======

Testing should be required for all source code. While there are many
tools available for testing python code ``pytest`` in my option is the
clear winner. I beleive this is due to ``pytest`` being the most
pythonic framework for testing. PyTest gives a guide on `integrating
it into your project
<https://docs.pytest.org/en/latest/goodpractices.html>`_. The
following will give a setup that is both simple and
opinionated. Another easy win we can get with pytest is code
coverage. We will use the add-on package ``pytest-cov`` for this.

--------
setup.py
--------

.. code-block:: python

   setup(
     ...
     setup_requires=['pytest-runner', ...],
     tests_require=['pytest', 'pytest-cov'],
   )

---------
setup.cfg
---------

::

   [aliases]
   test=pytest

That is all you need to get ``pytest`` running! You can run all tests
via the command ``python setup.py test`` or ``py.test``. Now that is
all assuming you have tests. ``pytest`` by default will look for tests
in the ``tests`` directory and runs all files with the name
``test_<filename>.py``. In order to get the additional coverage report
with the tests you need to add some additional arguments ``python
setup.py test --addopts "--cov=pypkgtemp"``.  Read the `pytest
documentation <https://docs.pytest.org/en/latest/>`_ for more detailed
documentation . For example create a file ``tests/test_example.py``
with the following code.

--------------------
test/test_example.py
--------------------

.. code-block:: python

   def test_example():
       assert 1 == 1

Now run the test via ``python setup.py test`` and you should see that
one test passes. Similarly how we discussed that all new tags of our
project should be pushed to PyPi we should also test all commits when
they are pushed to gitlab. Adding to the ``.gitlab-ci.yml`` setup in
the :doc:`pypi`_ documentation.

--------------
.gitlab-ci.yml
--------------

.. code-block:: yaml

   stages:
     - test
     - deploy

   test:
     image: python:3.6
     stage: test
     script:
       - pip install .
       - pip list
       - python setup.py test --addopts "--cov=<package-directory>"

With these changes it will test every commit given to Gitlab and will
only submit a new package if all tests pass! All of this has been
automated for us. In order to get the coverage report setup correctly
you will need to tell gitlab the regular expression to use in order to
parse the coverage report. For ``pytest-cov`` this is
``^TOTAL\s+\d+\s+\d+\s+(\d+)\%\s*$``.
