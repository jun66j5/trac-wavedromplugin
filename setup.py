#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Jun Omae
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from setuptools import setup, find_packages

extra = {}

setup(
    name='TracWaveDromPlugin',
    version='0.1',
    packages=find_packages(exclude=['*.tests']),
    package_data={'tracwavedrom' : ['htdocs/*.*', 'htdocs/*/*.*']},
    author='Jun Omae',
    author_email='jun66j5@gmail.com',
    license='3-clause BSD',  # the same as Trac
    url='http://trac-hacks.org/wiki/WaveDromPlugin',
    description='Provides WaveDrom processor to render wavedrom drawings within Trac wiki page',
    entry_points={'trac.plugins': [
        'tracwavedrom.macro = tracwavedrom.macro',
        ]},
    install_requires=['Trac >= 0.11'],
    tests_require=[],
    **extra)
