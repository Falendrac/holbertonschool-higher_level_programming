#!/usr/bin/python3
'''
fetches https://intranet.hbtn.io/status
'''

import requests


def main():
    '''
    Main function
    '''
    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}".format(
        type(req.text), req.text))


if __name__ == '__main__':
    main()
