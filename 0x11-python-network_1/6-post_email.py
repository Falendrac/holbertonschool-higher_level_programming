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
    email = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data = email)
    print(req.text)


if __name__ == '__main__':
    main()
