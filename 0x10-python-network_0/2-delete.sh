#!/bin/bash
# sends a DELETE request to the URL passed as the first argument and displays the body of the response
if [ $# -ge 1 ]
    then
        curl -X "DELETE" "${1}"
fi
