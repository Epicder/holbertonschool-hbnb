#!/bin/bash

URL="http://localhost:5000/users"

pkill -f "python3"
python3 ../Run.py & > /dev/null
sleep 1

create_user() {
    DATA="{
    \"email\": \"$RANDOM@example.com\",
    \"first_name\": \"usu\",
    \"last_name\": \"ario\"
    }"

    curl -fsSL -X POST $URL \
    -H "Content-Type: application/json" \
    -d "$DATA"
}

get_user() {
    echo "Test get user at '$URL/$1'"
    curl $URL/$1
}

get_users() {
    echo "Test get all users at '$URL'"
    curl $URL
}

update_user() {
    DATA="{
    \"email\": \"$RANDOM@example.com\",
    \"first_name\": \"ma\",
    \"last_name\": \"rio\"
    }"

    curl -fsSL -X PUT $URL/$1 \
    -H "Content-Type: application/jason" \
    -d "$DATA"
}

delete_user() {
    echo "Test delete a user at '$URL/$1'"
    curl -X DELETE $URL/$1
}

user=$(create_user)

ID=$(echo $user | python3 -m json.tool | grep -o '"id": *"[^"]*"' | cut -d '"' -f 1| paste)

echo "retured id: $ID"
#create_user
get_user $ID
get_users
update_user $ID
delete_user $ID

pkill -f "python3"
