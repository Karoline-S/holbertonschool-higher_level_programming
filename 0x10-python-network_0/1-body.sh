#!/usr/bin/env bash
# sends a request to passed in URL, displays body of responses with status code 200

status_code=$(curl -sw "%{http_code}" "$1" | sed 's/[^0-9]*//g')

if [ "$status_code" == "200" ]
then
    curl "$1"
fi
