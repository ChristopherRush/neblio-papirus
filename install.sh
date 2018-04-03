#!/usr/bin/env bash

sudo apt-get update

sudo apt-get install pip, git

pip install python-bitcoinrpc

git clone https://github.com/ChristopherRush/stakebox-papirus.git

file=/home/pi/.neblio/neblio.conf
if [ -e "$file" ]; then
    echo "File exists"
else
    echo "File does not exist"
fi
