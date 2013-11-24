#!/usr/bin/env python
# -*- coding: UTF8 -*-
'''
justicker.archivist
~~~~~~~~~~~~~~~~~~~

Archivist fetches the stock data and stores it to a database.

:copyright: (c) 2013, Douglas Watson <douglas@watsons.ch>
:license: MIT license, see LICENSE for more information

'''

from datetime import datetime
import requests
from pymongo import MongoClient

MARKET_URL = "https://api.justcoin.com/v1/markets"

DB_CONFIG = {
    'database': 'justicker',
    'host': 'localhost',
    'port': None,
}

def get_markets():
    ''' Returns json data for markets as unicode string '''

    response = requests.get(MARKET_URL)
    data = response.json()

    time = datetime.utcnow() # timestamp shouldn't depend on timezone
    # Add a timestamp to each field
    for entry in data:
        entry['timestamp'] = time

    return data


def archive_data(data, collection='markets'):
    ''' Archives the dictionary to a MongoDB database.

    :arg dict data: dictionary of data to store
    :arg string collection: collection to store data in

    '''

    client = MongoClient(DB_CONFIG['host'])
    db = client[DB_CONFIG['database']]
    coll = db[collection]
    coll.insert(data)

def present_markets(id='BTCEUR'):
    ''' Retrieves market data from database and prepares it for plotting 

    :arg string id: id string of the desired market. 

        One of: BTCEUR, BTCLTC, BTCNOK, BTCUSD, BTCXRP

    :returns: arrays of : dates, last, high, low, bid, ask, volume, scale
    '''

    client = MongoClient(DB_CONFIG['host'])
    db = client[DB_CONFIG['database']]
    coll = db['markets']

    # entries = coll.find({'id': id})
    entries = coll.find()
    print entries()

    dates = [ e['date'] for e in entries ]
    last = [ e['last'] for e in entries ]
    high = [ e['high'] for e in entries ]
    low = [ e['low'] for e in entries ]
    bid = [ e['bid'] for e in entries ]
    ask = [ e['ask'] for e in entries ]
    volume = [ e['volume'] for e in entries ]
    scale = [ e['scale'] for e in entries ]

    return dates, last, high, low, bid, ask, volume, scale




if __name__ == '__main__':

    # data = get_markets()
    # archive_data(data, database='justicker-testing')
    print present_markets()
