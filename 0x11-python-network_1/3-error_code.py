#!/usr/bin/python3
'''
takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
'''

from urllib import request, error
import sys


def main():
    '''
    Main function
    '''
    try:
        with request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))

if __name__ == '__main__':
    main()
