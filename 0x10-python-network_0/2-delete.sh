#!/usr/bin/env bash
# sends a DELETE request to the passed in url

curl -s "$1" -X DELETE
