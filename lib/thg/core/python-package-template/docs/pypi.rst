PyPi
====

PyPi otherwise known as the cheeseshop is the packaging repository for
python. PyPi has been going through some great changes recently
including a new UI and not requiring registering new projects. PyPi
deployment can seem daunting. `Twine <https://github.com/pypa/twine>`_
is your best friend.

PyPi has two repositories. The `testing repository
<https://test.pypi.org/>`_ and `main repository
<https://pypi.org>`_. when you are trying out deploying packages I
would advise starting with testing. Older guides for using PyPi will
state that you need to pre-register a package. This is no longer the
case.

First you will need to create a pypi account. The testing and
production repositories require separate accounts. Look for the
Register link in the top right of the site.  After creating your
account keep track of the ``username`` and ``password``.

From this point we have everything needed to do a simple manual
deployment to pypi. If you dont want to submit to the testing
repository remove ``--repository-url
https://test.pypi.org/legacy/``. You will be prompted for your
username and password.

1. ``pip install twine``
2. ``python setup.py sdist bdist_wheel``
3. ``twine upload --repository-url https://test.pypi.org/legacy/ dist/*``

This is easy! But one issue is that this process is not
automated. Really we would like anytime that we create a new release
on git that it is pushed to pypi. This is where Gitlab comes to the
rescue.

Gitlab has a continuous deployment and continuous integration pipeline
that is free to use. This will only work for code that is stored in a
Gitlab repo.

Add the following to a ``.gitlab-ci.yml`` file in the root of your
project. The reason that there are two twine upload steps is because
there is currently a flaw in the markdown processing (`issue
<https://github.com/di/markdown-description-example/issues/1>`_). Hopefully
this is fixed soon.

--------------
.gitlab-ci.yml
--------------

.. code-block:: yaml

   variables:
     TWINE_USERNAME: SECURE
     TWINE_PASSWORD: SECURE
     TWINE_REPOSITORY_URL: https://test.pypi.org/legacy/

   stages:
    - deploy

   deploy:
     image: python:3.6
     stage: deploy
     script:
       - pip install -U twine setuptools
       - pip list
       - python setup.py sdist bdist_wheel
       - twine upload dist/*.tar.gz
       - twine upload dist/*.whl
     only:
       - /^v\d+\.\d+\.\d+([abc]\d*)?$/  # PEP-440 compliant version (tags)

Additionally ``settings->CI/CD->Secret variables`` the environment
variables ``TWINE_PASSWORD`` and ``TWINE_USERNAME`` need to be set. At
this point whenever a git tag of the form ``vX.Y.Z`` is pushed to
Gitlab a new version will be pushed to PyPi. Make sure that your git
tags match the version number! PyPi does not allow you to change a
currently existing version of your project. This is a good thing since
we should all do our best to follow `semantic versioning
<https://semver.org/>`_.

Once you would like to deploy to the main PyPi repository change
``TWINE_REPOSITORY_URL`` to ``https://upload.pypi.org/legacy/``.

So you now have a package that can be shared with the entire world!
But you have no testing... the next section :doc:`testing` will show
you how to include testing via ``pytest``.

Further Information
-------------------

sdist
^^^^^
``sdist`` stands for source distribution and is the old python packaging
format used since 2003. It does not have an official format. It
basically takes files in the current directory and archives them for
distribution. That this format is not good for shared libraries as in
does not work. It is basic and cross platform in the sense that all c
extensions must be compiled by the host OS. ``MANIFEST.in`` is an
important file that determines which files are included. Further
details on a source distribution can be `found here
<https://docs.python.org/3.6/distutils/sourcedist.html#specifying-the-files-to-distribute>`_.

wheels
^^^^^^

Wheels are truly a step up in python packaging. They are built by
``python setup.py bdist_wheel``. It is `standardized
<https://www.python.org/dev/peps/pep-0427/>`_ and can be a true
packaging format. All packages are platform specific. So if you build
a binary for linux it can only be shared with other linux computers.

I will update further once I have packaged a shared library using
wheels.
