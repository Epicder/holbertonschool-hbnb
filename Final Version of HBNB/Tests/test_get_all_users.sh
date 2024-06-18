#!/bin/bash

python3 ../wsgi.py & sleep 1

URL="http://localhost:8000/users"

curl -X GET $URL \
-H "Content-Type: application/json"
pkill -f "python run.py"