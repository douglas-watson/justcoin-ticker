Justicker - Justcoin Ticker
===========================

A stock ticker for Justcoin

:Copyright: (c) 2013, Douglas Watson
:License: MIT License


Introduction
------------

This is mostly an excuse to make a web service client, use a noSQL database, and
potentially play with some new visualization tools. I admit some choices do not
make sense for a stock ticker --- a noSQL database makes no sense with  highly-
structued, purely numerical data. I'm doing it to play with those techniques, and maybe see how well they work for this.

The motivations for a Justcoin stock ticker are simple:

1. You must login to consult the rates
2. Justcoin provides a simple API

The lame name is to avoid any name conflicts with ticker.

Requirements
------------

Python, MongoDB.

Python is used to query the API, MongoDB stores the data, and Flask (python web
framework) provides the web frontend.

Installation
------------

Deploy the usual way for a Flask app.