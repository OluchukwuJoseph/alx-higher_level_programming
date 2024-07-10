#!/usr/bin/python3
"""This script sends a request to the URL passed"""
from urllib import request
import sys


if __name__ == '__main__':
    req = request.Request(sys.argv[1])
    with request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
