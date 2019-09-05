**All issues and contributions should be done on
[Gitlab](https://gitlab.com/costrouc/python-package-template). Github
is used only as a mirror for visibility**

# Python Package Template

<table>
<tr>
  <td>Latest Release</td>
  <td><img src="https://img.shields.io/pypi/v/pypkgtemp.svg" alt="latest release" /></td>
</tr>
<tr>
  <td></td>
  <td><img src="https://anaconda.org/costrouc/pypkgtemp/badges/version.svg" alt="latest release" /></td>
</tr>
<tr>
  <td></td>
  <td>
    <a href="https://hub.docker.com/r/costrouc/python-package-template/">
    <img src="https://img.shields.io/badge/docker-latest-blue.svg" alt="latest release" />
    </a>
  </td>
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
    <img src="https://media.readthedocs.org/static/projects/badges/passing.svg" alt="readthedocs documentation" />
    </a>
  </td>
</tr>
</table>

This is an opinionated attempt to document how I deploy a python
application with documentation, testing, pypi, and continuous
deployment. This project will be updated as I change my python
development practices. Number one this is a learning experience.

 - documentation ([sphinx](http://www.sphinx-doc.org/en/stable/), selfhosted + [readthedocs](https://readthedocs.org/))
 - testing ([pytest](https://docs.pytest.org/en/latest/)) and coverage ([pytest-cov](https://github.com/pytest-dev/pytest-cov))
 - deploy to pypi ([twine](https://github.com/pypa/twine))
 - deploy to conda ([conda](https://github.com/conda/conda))
 - deploy docker container to ([dockerhub](https://hub.docker.com) and [gitlab container registry](https://about.gitlab.com/2016/05/23/gitlab-container-registry/))
 - building a package (`setup.py`, `README.md`, `CHANGELOG.md`, `LICENSE.md`)
 - command line interface with argparse
 - badges for testing, packages, and documentation

## Assumptions:

Gitlab will be used for the continuous deployment. It is a great
project that is open source and comes with many nice features not
available for Github. You should consider it! Features used:

 - [pages](https://docs.gitlab.com/ee/user/project/pages/index.html)
 - [CI/CD](https://about.gitlab.com/features/gitlab-ci-cd/)

If you would like a custom domain setup with gitlab pages for the
documentation you will need to use
[cloudflare](https://www.cloudflare.com/). I have a [blog written on
how to do
this](https://chrisostrouchov.com/posts/hugo_static_site_deployment/)
or you can look at the [gitlab cloudflare
documentation](https://about.gitlab.com/2017/02/07/setting-up-gitlab-pages-with-cloudflare-certificates/).

## Steps

This project is a python package itself and full documentation is
available on readthedocs. Each of the steps below includes a link to
the section in the documentation.

1. [setup a bare python package](https://costrouc-python-package-template.readthedocs.io/en/latest/packaging.html) with git repo (`setup.py`, `README.md`, `.gitignore`, `<package>`)
2. [setup pypi deployment](https://costrouc-python-package-template.readthedocs.io/en/latest/pypi.html) with git tags `vX.X.X`
3. [setup testing](https://costrouc-python-package-template.readthedocs.io/en/latest/testing.html) on each commit with `pytest`
4. [setup documentation](https://costrouc-python-package-template.readthedocs.io/en/latest/documentation.html) with `sphinx` on readthedocs and self hosted

# Requirements

None!

# Contributing

All contributions, bug reports, bug fixes, documentation improvements,
enhancements and ideas are welcome. These should be submitted at the
[Gitlab repository](https://gitlab.com/costrouc/python-package-template). Github is
only used for visibility.

The goal of this project is to in an opinionated way guide modern
python packaging development for myself.

# License

MIT
