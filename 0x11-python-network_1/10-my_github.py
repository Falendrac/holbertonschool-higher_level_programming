#!/usr/bin/python3
'''
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
'''

import requests
from requests.auth import HTTPBasicAuth
import sys


def main():
    '''
    Main function
    '''
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]
    req = requests.get(url, auth=(username, token))

    api_info = req.json()

    if 'id' in api_info:
        print(api_info['id'])
    else:
        print("None")


if __name__ == '__main__':
    main()
