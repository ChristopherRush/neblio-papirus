#!/usr/bin/env bash

sudo apt-get update

sudo apt-get install pip, git

pip install python-bitcoinrpc

git clone https://github.com/ChristopherRush/stakebox-papirus.git

RPCPASSWORD=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)

neblioqt=/home/pi/Desktop/neblio-qt

if [ -e "$neblioqt" ]; then
    echo "neblio installed....checking config file"
    neblio=/home/pi/.neblio/neblio.conf
    if [ -e "$neblio" ]; then
        echo "Config file already exists at $neblio"
    else
        echo "File does not exist"
        touch $neblio
        echo "neblio.conf file created"
        echo "[config]" >> $neblio
        RPCPASSWORD=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
        echo "rpcpassword=$RPCPASSWORD" >> $neblio
        echo "rpcuser=nebliorpc" >> $neblio
        echo "rpcport=8332" >> $neblio
        echo "rpcallowip=127.0.0.1" >> $neblio
        echo "configuration settings appended"
    fi
else
    echo "neblio not installed on this StakeBox"

fi
