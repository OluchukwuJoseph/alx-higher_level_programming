#!/usr/bin/python3
"""This script fetches https://alx-intranet.hbtn.io/status"""
from urllib import request


if __name__ == '__main__':
    req = request.Request('https://alx-intranet.hbtn.io/status')
    with request.urlopen(req) as response:
        print('Body response:')
        print('\t- type: {}'.format(type(response.read())))
        print('\t- content: {}'.format(response.read()))
        print('\t- utf8 content: {}'.format(response.status))
