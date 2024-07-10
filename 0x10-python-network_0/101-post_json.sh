#!/bin/bash
# This script send a POST request with the contents of a jsom file
curl -sX POST -H "Content-Type: application/json" --data-binary @"$2" "$1"
