#!/usr/bin/python3
"""
    This script  takes in a URL and an email
    sends a POST request to the passed URL with the email as a parameter
"""
from urllib import request
from urllib import parse
import sys


if __name__ == '__main__':
    params = {'email': sys.argv[2]}
    data = parse.urlencode(params)
    data = data.encode('ascii')

    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        print(response.read())
