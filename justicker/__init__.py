#!/usr/bin/env python
# -*- coding: UTF8 -*-
'''
justicker
~~~~~~~~~

A stock ticker for the Justcoin trading platform. Web front-end in Flask, data
stored in MongoDB.

This "main" script manages configuration, the web server, and scheduled tasks.

:copyright: (c) 2013, Douglas Watson <douglas@watsons.ch>
:license: MIT license, see LICENSE for more information

'''

from flask import Flask
from kronos import ThreadedScheduler, method

app = Flask(__name__)
app.config.from_object('justicker.config')

from justicker import archivist     # the 'controller' or 'data manager'
from justicker import presenter     # the 'views'

__all__ = ['app']

############################################
# Setup repeated tasks
############################################

def record_markets():
    ''' Get and store market data. To be scheduled by kronos. '''
    data = archivist.get_markets()
    archivist.archive_data(data)

#: Manages repeated tasks, such as fetching new data
app.scheduler = ThreadedScheduler()

# Fetch stock data every 1 hour
app.scheduler.add_interval_task(action=record_markets, 
    taskname='get_markets', initialdelay=0, interval=60, 
    processmethod=method.threaded, args=None, kw=None)

############################################
# Main
############################################

if __name__ == '__main__':
    app.scheduler.start()
    app.run('localhost', debug=True)
    app.scheduler.stop()
