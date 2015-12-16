#!/usr/bin/env python
# -*- coding: utf-8 -*-

r'''
setup for github-images
'''

__author__ = "Osamu Sugiyama"
__author_email__ = "sugiyama.o@gmail.com"
__date__ = "2015/11/17"
__version__ = "0.0.1b"

import os
from setuptools import setup, find_packages


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except:
        return ''

setup(
    name='gihub-images',
    version='0.0.1b',
    description='',
    author=__author__,
    author_email=__author_email__,
    url='',
    scripts=['git-images', ],
    long_description=__doc__,
    include_package_data=True,
    install_requires=[
        'click',
        'gitpython'
    ],
    zip_safe=False
)
