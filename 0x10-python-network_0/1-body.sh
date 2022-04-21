#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
if [ $# -ge 1 ]
    then
        curl -sL "${1}"
fi
