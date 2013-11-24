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

import os
import sys
import json
from pymongo import MongoClient

# Add project root directory to path
p = os.path
basedir = p.abspath(p.dirname(__file__))
rootdir = p.abspath(p.join(p.dirname(__file__), p.pardir, p.pardir))
# sys.path.insert(0, rootdir)

from justicker import app
from justicker.archivist import archive_data, present_markets


class TestArchivist(object):

    def setUp(self):

        client = MongoClient('localhost')
        self.db = client['justickler-tests']

        # Insert some testing data
        import cPickle as pickle
        with open(os.path.join(basedir, 'test_data.pickle'), 'r') as fo:
            test_data = pickle.load(fo)

        self.db.markets.insert(test_data)

    def tearDown(self):
        ''' Delete all test data '''

        # Delete 
        self.db.markets.drop()



    def test_archive_stores_data(self):
        ''' Make sure an example piece of JSON is stored properly '''

        num_entries = self.db.markets.count()

        with open(os.path.join(basedir, 'example_markets.json')) as fo:
            data = json.load(fo)

        archive_data(data, collection='markets', db=self.db)

        # check the data was stored right
        new_num_entries = self.db.markets.count()

        # Should have added five entries:
        assert new_num_entries == num_entries + 5

    def test_present_markets(self):
        ''' Check present_markets extracts data correctly '''

        data = present_markets(id='BTCEUR', db=self.db)

        assert data['high'] == [675.000, 680.000]
        assert data['last'] == [595.230, 679.000]



