#!/usr/bin/env bash
# send a POST request to given url with variables

curl -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
