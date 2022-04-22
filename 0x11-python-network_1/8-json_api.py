#!/usr/bin/python3
'''
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
'''

import requests
import sys


def main():
    '''
    Main function
    '''
    if len(sys.argv) == 1:
        letter = {'q': ""}
    else:
        letter = {'q': sys.argv[1]}

    req = requests.post('http://0.0.0.0:5000/search_user', data=letter)

    try:
        in_json = req.json()
        if len(in_json) > 0:
            print("[{}] {}".format(in_json['id'], in_json['name']))
        if len(in_json) == 0:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == '__main__':
    main()
