#!/usr/bin/env python
# -*- coding: UTF8 -*-
'''
justicker.presenter
~~~~~~~~~~~~~~~~~~~

Web front-end for the stock ticker. This would be the "views" components of a
Django-like MVT framework.

:copyright: (c) 2013, Douglas Watson <douglas@watsons.ch>
:license: MIT license, see LICENSE for more information

'''

from flask import Flask

from __init__ import app

app.route('/')
app.route('/index')
def index():
    ''' Feed landing page ''' 
    pass
