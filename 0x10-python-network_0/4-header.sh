#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
if [ $# -ge 1 ]
    then
        curl -sH 'X-School-User-Id: 98' "$1"
fi
