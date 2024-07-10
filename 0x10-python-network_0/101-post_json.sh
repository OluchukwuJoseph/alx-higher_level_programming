#!/bin/bash
# This script send a POST request with the contents of a jsom file
curl -sX POST --data-binary @"$2" "$1"
