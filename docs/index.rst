.. Justcoin Ticker documentation master file, created by
   sphinx-quickstart on Sat Nov 23 12:08:33 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

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
structued, purely numerical data. I'm doing it to learn the technologies.

The motivation for a Justcoin stock ticker is twofold:

1. You must login to consult the rates
2. Justcoin provides a simple API

Requirements
------------

Python, MongoDB.

Python is used to query the API, MongoDB stores the data, and Flask (python web
framework) provides the web frontend.

Installation
------------

Install Python and MongoDB. On ubuntu::

    sudo apt-get install python-setuptools mongodb

Run the setup script::

    python setup.py install

It should install all dependencies.

.. toctree::
   :maxdepth: 2

   design
   data_structures
   api



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

