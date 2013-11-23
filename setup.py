#!/usr/bin/env python
# -*- coding: UTF8 -*-
'''
justicker
~~~~~~~~~

A stock ticker for the Justcoin trading platform. Web front-end in Flask, data
stored in MongoDB.

:copyright: (c) 2013, Douglas Watson <douglas@watsons.ch>
:license: MIT license, see LICENSE for more information

'''

from setuptools import setup

setup(
    name='Justcoin Stock Ticker',
    description='Web stock ticker for Justcoin',
    version='0.1dev',
    author='Douglas C. Watson',
    author_email='douglas@watsons.ch',
    packages=['justicker',],
    license='MIT',
    long_description=open('README.rst').read(),
    install_requires=[
    	'flask',
        'requests',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
