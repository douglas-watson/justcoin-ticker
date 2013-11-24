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
# from kronos import ThreadedScheduler

app = Flask(__name__)
app.config.from_object('justicker.config')

from justicker import archivist     # the 'controller' or 'data manager'
from justicker import presenter     # the 'views'

__all__ = ['app']

############################################
# Setup and config
############################################

#: Manages repeated tasks, such as fetching new data
# app.scheduler = ThreadedScheduler()

# Fetch stock data every 1 hour
# app.scheduler.add_interval_task(archivist.get_markets, 'get_markets', ...)

############################################
# Main
############################################

if __name__ == '__main__':
    # app.scheduler.start()
    app.run('localhost', debug=True)
    # app.scheduler.stop()
