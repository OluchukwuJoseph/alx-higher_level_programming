#!/usr/bin/env bash
# This script sends a DELETE request to the URL passed as the first argument
# and displays the body of the response

curl -sL -X DELETE "$1"
