#!/usr/bin/python3
"""
    This script  takes in a URL and an email
    sends a POST request to the passed URL with the email as a parameter
"""
import requests
import sys


if __name__ == '__main__':
    params = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], params)
    print(response.text)
