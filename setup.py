#!/usr/bin/env python
from os.path import join
import re
from setuptools import setup

# dynamically pull the version from cloudprinting/__init__.py
with open(join('googleprint', '__init__.py'), 'r') as f:
    version = re.search('^__version__ = "(.+?)"$', f.read(), re.MULTILINE).group(1)

setup(
    name='googleprint',
    version=version,
    description='Simple API for Google Cloud Print',
    author='Jayden Smith',
    author_email='jayden@intelliscale.com.au',
    url='http://pypi.python.org/pypi/googleprint/',

    packages=['googleprint'],
    include_package_data=True,  # declarations in MANIFEST.in

    install_requires=['requests'],

    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
    ],
)
