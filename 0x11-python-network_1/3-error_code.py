#!/usr/bin/python3
"""This script sends a request to the URL passed"""
from urllib import request, error
import sys

if __name__ == '__main__':
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as response:
            body = response.read()
            print(body)
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
