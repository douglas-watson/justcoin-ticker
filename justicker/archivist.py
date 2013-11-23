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

def get_markets():
    ''' Returns json data for markets as unicode string '''

    response = requests.get(MARKET_URL)
    data = response.json()

    time = datetime.utcnow() # timestamp shouldn't depend on timezone
    # Add a timestamp to each field
    for entry in data:
        entry['timestamp'] = time

    return data


def archive_data(data, collection='markets', 
                            database='justicker', host='localhost'):
    ''' Archives the dictionary to a MongoDB database.

    :arg dict data: dictionary of data to store
    :arg string host: address of server running MongoDB
    :arg string database: name database to use
    :arg string collection: collection to store data in

    '''

    client = MongoClient(host)
    db = client[database]
    coll = db[collection]
    coll.insert(data)

if __name__ == '__main__':

    data = get_markets()
    archive_data(data, database='justicker-testing')