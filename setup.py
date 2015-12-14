#!/usr/bin/env python
# -*- coding: utf-8 -*-

r'''
sound source identification package using hark.
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
    # package_dir={'': 'src'},
    # packages=find_packages('src'),
    # package_data={
    #     '': [
    #         'ssi/rpca/*.m',
    #         'ssi/rpca/inexact_alm_rpca/*.m',
    #         'ssi/rpca/inexact_alm_rpca/PROPACK/*.m',
    #         'ssi/simulation/*.m',
    #         'ssi/sss_network/config/*',
    #         'ssi/sss_network/networks/*.n',
    #     ]
    # },
    # namespace_packages=['pyhark'],
    long_description=__doc__,
    include_package_data=True,
    install_requires=[
        'click',
        # 'oct2py',
        # 'numpy',
        # 'scipy',
        # 'matplotlib',
        # 'chainer',
        # 'theano',
        # 'features'
        # 'sklearn'
    ],
    zip_safe=False
)
