#!/usr/bin/env python
# -*- coding: UTF8 -*-
'''
justicker.archivist
~~~~~~~~~~~~~~~~~~~

Archivist manages the fetching of remote data, as interacting with the database.

:copyright: (c) 2013, Douglas Watson <douglas@watsons.ch>
:license: MIT license, see LICENSE for more information

'''

import requests
import numpy as np
from datetime import datetime
from pymongo import MongoClient

from justicker import app

__all__ = ['get_markets', 'archive_data', 'present_markets', 'DB']

#: API URL for Markets feed
MARKETS_URL = 'https://api.justcoin.com/v1/markets'

#: database client
client = MongoClient(app.config['DB_HOST'])
DB = client[app.config['DATABASE']]

def time_to_milliseconds(time):
    ''' Return time in milliseconds, for JSON '''

    epoch = datetime.utcfromtimestamp(0)
    delta = time - epoch
    unix_time = delta.total_seconds()

    return int(unix_time * 1000)
    

def get_markets():
    ''' Returns json data for markets as unicode string '''

    response = requests.get(MARKETS_URL)
    data = response.json()

    time = datetime.utcnow() # timestamp shouldn't depend on timezone
    # Add a timestamp to each field
    for entry in data:
        entry['timestamp'] = time

    return data


def archive_data(data, collection='markets', db=DB):
    ''' Archives the dictionary to a MongoDB database.

    :arg dict data: dictionary of data to store
    :arg string collection: collection to store data in
    :arg pymongo.Database database: database object to store data in

    '''

    coll = db[collection]
    coll.insert(data)

def present_markets(id='BTCEUR', db=DB):
    ''' Retrieves market data from database and prepares it for plotting 

    :arg string id: id string of the desired market. 

        One of: BTCEUR, BTCLTC, BTCNOK, BTCUSD, BTCXRP

    :arg pymongo.Database database: database object to use 

    :returns: a dictionary containing several arrays::

        { 
            'id': 'BTCEUR', # string
            'dates' : [..., ...],   # datetime.datetime object
            'last' : [..., ...],    # floats
            'high' : [..., ...],    # floats
            'low' : [..., ...],     # floats
            'bid' : [..., ...],     # floats
            'ask' : [..., ...],     # floats
            'volume' : [..., ...],  # floats
            'scale' : [..., ...],   # ints
        }

    '''

    coll = db['markets']

    # Need to cast to list to iterate more than once.
    entries = list(coll.find({'id': id}).sort('date'))

    # TODO translate to something Highcharts can use.

    data = np.array([[
        e['timestamp'],
        float(e['last']), 
        float(e['low']), 
        float(e['high'])]
            for e in entries ])

    # Make 'open' col and insert as second column
    open_col = np.append(data[0, 1], data[:-1,1])
    data = np.insert(data, 1, open_col, axis=1)

    # Convert timestamps to milliseconds for highcharts:
    dates = map(time_to_milliseconds, data[:,0])
    data[:,0] = dates

    return data.tolist()


if __name__ == '__main__':

    # data = get_markets()
    # archive_data(data)
    print present_markets()
