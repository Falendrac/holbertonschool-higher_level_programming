#!/usr/bin/python3
'''
takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body
of the response (decoded in utf-8)
'''

from urllib import request, parse
import sys


def main():
    '''
    Main function
    '''
    data = {'email': sys.argv[2]}
    data = parse.urlencode(data).encode()
    req = request.Request(sys.argv[1], data=data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))


if __name__ == '__main__':
    main()
