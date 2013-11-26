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
    app.run('localhost', debug=True)