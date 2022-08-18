#!/bin/bash
# makes request to a url using PUT method and updating data and header
curl -sLX PUT -d "user_id=98" 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool"
