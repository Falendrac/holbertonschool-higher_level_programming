#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
if [ $# -ge 1 ]
    then
        curl -sI "${1}" | grep  Allow | cut -c 8-
fi
