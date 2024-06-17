#!/bin/bash

python run.py & sleep 5

URL="http://localhost:5000/users"

curl -X GET $URL \
-H "Content-Type: application/json"
pkill -f "python run.py"