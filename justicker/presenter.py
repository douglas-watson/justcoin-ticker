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

from flask import render_template, jsonify, Response

from justicker import app
from justicker import archivist

@app.route('/')
@app.route('/index')
def index():
    ''' Feed landing page ''' 
    return render_template('index.html')

@app.route('/api/markets/<id>')
def market(id):
    ''' Return JSON data for market ``id`` '''

    # Get data from archivist
    data = archivist.present_markets(id)

    # Prepare response
    resp = jsonify({'data': data})
    resp.status_code = 200

    return resp
