#!/usr/bin/env python
# -*- coding: UTF8 -*-
'''
runserver.py
~~~~~~~~~~~~

Start serving the web service

:copyright: (c) 2013, Douglas Watson <douglas@watsons.ch>
:license: MIT license, see LICENSE for more information

'''

from justicker import app 

if __name__ == '__main__':
    app.scheduler.start()
    app.run('0.0.0.0', port=8899, debug=True)
    app.scheduler.stop()


