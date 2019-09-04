=====
Conda
=====

Conda is an alternative package manger to PyPi. It comes with many
features that PyPi packaging does not handle well such as including
compiled libraries and c dependencies.

While traditional Python packages are stored in `pypi.org
<https://pypi.org>`_ conda python packages are stored at `anaconda.org
<https://anaconda.org>`_. These steps do not require that you have
already deployed a package to PyPi.

First create an account through `https://anaconda.org
<https://anaconda.org>`. Unlike PyPi there is no test repo to submit
your package to. Anaconda takes a different philosophy where each user
has a collection of packages and jupyter notebooks in their repo. The
approach I will show you does not require that you have ``conda``
installed on your machine.  If you would like to experiment with the
build tool I would recommend pulling the continuum ``conda build``
docker container `continuumio/miniconda3
<https://hub.docker.com/r/continuumio/miniconda3>`_. The default
`continuumio/anaconda3` docker environment is over 3.5 GB
unzipped. Why are the continuum docker containers so large?

.. code-block:: shell

   docker pull continuumio/miniconda3
   docker run -i -t continuumio/miniconda3 /bin/bash

Once you start the docker container you can do the following steps for
package deployment to conda. These steps will be automated later with
a Gitlab build script. In order to upload packages you will either
need to login to your account via ``anaconda login`` or create an
account token will all account access. I would recommend creating an
account token so that you can revoke access at any time. To create an
account token go to ``settings->access`` on anaconda.org when you are
logged in.

1. `conda install anaconda-client setuptools conda-build -y`
2. `python setup.py bdist_conda`
3. `anaconda -t $ANACONDA_TOKEN upload -u $ANACONDA_USERNAME /opt/conda/conda-bld/linux-64/<package>-<version>-<pyversion>.tar.bz2`

The first step ensures that all packages are the right version and we
have the command line anaconda tool. Anaconda has it hidden in their
documentation that they have a convenient `build tool for python
packages
<https://conda.io/docs/user-guide/tasks/build-packages/build-without-recipe.html>`_
that does not require a recipe. When running in a conda environment
they have overridden setuptools to include `bdist_conda` for building
conda packages. The build command will build the package, run tests,
and check that each command created exits. After your package is built
you can now upload to conda. If you are building within a docker
container chances are that their is only one conda build so you can
shorten the upload command to `anaconda upload
/opt/conda/conda-bld/linux-64/<package>*.tar.bz2`. Otherwise you will
have to chose the build that is provided at the end of the ``python
setup.py bdist_conda`` output.

From some of my initial tests I was surprised that many packages
available on PyPi are not available on `conda` and thus made the
builds fail. These errors are most likely due to me know understanding
the conda tools well. If your build succeeded you should see the
package listed on `https://anaconda.org/<username>`.

Since we are all about automation lets make this process automatic on
Gitlab!

.. code-block:: yaml

   variables:
     TWINE_USERNAME: SECURE
     TWINE_PASSWORD: SECURE
     TWINE_REPOSITORY_URL: https://test.pypi.org/legacy/
     ANACONDA_USERNAME: SECURE
     ANACONDA_TOKEN: SECURE

   stages:
    - deploy

   deploy_conda:
     image: continuumio/miniconda3:latest
     stage: deploy
     script:
       - conda install anaconda-client setuptools conda-build -y
       - python setup.py bdist_conda
       - anaconda -t $ANACONDA_TOKEN upload -u $ANACONDA_USERNAME /opt/conda/conda-bld/linux-64/pypkgtemp*.tar.bz2
     only:
       - /^v\d+\.\d+\.\d+([abc]\d*)?$/  # PEP-440 compliant version (tags)
