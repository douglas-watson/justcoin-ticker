#!/usr/bin/env python
# -*- coding: UTF8 -*-
'''
tests.test_archivist
~~~~~~~~~~~~~~~~~~~~

Unit testing of the archivist module

The tests require a local running MongoDB

:copyright: (c) 2013, Douglas Watson <douglas@watsons.ch>
:license: MIT license, see LICENSE for more information

'''

from pymongo import MongoClient
from json import load

from justicker.archivist import 

class TestArchivist(object):

    def setUp():

        client = MongoClient('localhost')
        self.db = client['justicker-test']

    def test_archive_stores_data():
        ''' Make sure an example piece of JSON is stored properly '''

        data = json.load(open('justicker/tests/json'))
