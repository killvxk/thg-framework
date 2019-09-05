# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='pypkgtemp',
    version='1.2.0',
    description='A python package template',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.com/costrouc/knoxpy-sqlite-pypi-readthedocs',
    author='Chris Ostrouchov',
    author_email='chris.ostrouchov+pypkgtemp@gmail.com',
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='python package template documentation testing continuous deployment',
    packages=find_packages(exclude=['docs', 'tests']),
    setup_requires=['pytest-runner', 'setuptools>=38.6.0'],  # >38.6.0 needed for markdown README.md
    tests_require=['pytest', 'pytest-cov'],
    entry_points={
        'console_scripts': [
            'helloworld=pypkgtemp.__main__:main'
        ]
    }
)
