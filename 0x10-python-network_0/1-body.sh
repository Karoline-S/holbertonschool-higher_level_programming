#!/bin/bash
# sends a request to passed in URL, displays body of responses with status code 200
curl -s "$1" -L
