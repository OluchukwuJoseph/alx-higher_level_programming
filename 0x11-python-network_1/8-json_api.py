#!/usr/bin/python3
"""
    This script takes in a letter and sends a
    POST request to http://0.0.0.0:5000/search_user
"""
import requests
import sys


if __name__ == '__main__':
    data = {'q': sys.argv[1]}
    response = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        response_data = response.json()
        if response_data:
            print('[{}] {}'.format(response_data['id'], response_data['name']))
        else:
            print('No result')
    except Exception as e:
        print('Not a valid JSON')
