#!/bin/bash
# sends a request to a passed in URL and prints methods accepted
curl -sIX OPTIONS "$1" | grep -i Allow | sed -e 's/^Allow: //'
