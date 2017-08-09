Restaurant List Viewer
======================

This is a tool for converting *The Infatuation* restaurant imessage list shares (URLS) into a readable format.

Installation
------------
# Written in python2.7
# Need to backport lzma
sudo apt-get install liblzma-dev
pip install -r requirements.txt

Usage
-----
Simple command line
* ```python cli_list_viewer.py {:url}```

Process
-------

The imessage list shares have the format ```https://api.theinfatuation.com/services/v3/lists/{:id}?content={base64(lzma(pbf(:list)))}```
* Check for valid url
* Lift :id from url
* revert base64 encoding
* Uncompress lzma
* Process Protocol Buffer

Testing
-------

run ```python -m unittest tests.test_parser``` in the base directory
