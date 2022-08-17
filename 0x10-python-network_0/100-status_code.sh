#!/usr/bin/env bash
# outputs status_code from GET request on given URL

curl -s -o /dev/null -w "%{http_code}" "$1"
