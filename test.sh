#!/usr/bin/env bash
file=/home/pi/.neblio/neblio.conf
if [ -e "$file" ]; then
    echo "File exists"
else
    echo "File does not exist"
fi 
