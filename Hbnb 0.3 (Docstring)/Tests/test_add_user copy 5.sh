#!/bin/bash

python run.py & sleep 5

URL="http://localhost:5000/users"
DATA='{
  "email": "user@example.com",
  "password": "123",
  "first_name": "usu",
  "last_name": "ario"
}'

curl -X POST $URL \
-H "Content-Type: application/json" \
-d "$DATA"
pkill -f "python run.py"