#!/usr/bin/python3
'''
Open the intranet url and read it.
'''

import urllib.request


def main():
    '''
    Main function
    '''
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:\n\
    \t- type: {}\n\
    \t- content: {}\n\
    \t- utf8 content: {}".format(type(html), html, html.decode('utf-8')))


if __name__ == '__main__':
    main()
