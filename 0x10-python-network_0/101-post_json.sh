#!/bin/bash
# send json file in POST request to given URL
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
