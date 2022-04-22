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
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1])
    req = requests.get(url)
    api_info = req.json()

    for i in range(0, 10):
        print("{}: {}".format(api_info[i].get('sha'),
                              api_info[i].get('commit')
                              .get('author').get('name')))


if __name__ == '__main__':
    main()
