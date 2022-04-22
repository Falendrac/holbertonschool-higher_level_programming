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

    for commit in api_info[0:10]:
        print("{}: {}".format(commit.get('sha'),
                              commit.get('commit')
                              .get('author').get('name')))


if __name__ == '__main__':
    main()
