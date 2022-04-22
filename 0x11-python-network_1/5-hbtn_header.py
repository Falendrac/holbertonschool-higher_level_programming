#!/usr/bin/python3
'''
takes in a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header
'''

import requests
import sys


def main():
    '''
    Main function
    '''
    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-Id'))


if __name__ == '__main__':
    main()
