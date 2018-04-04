#!/usr/bin/env bash

RPCPASSWORD=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)

neblioqt=/home/pi/Desktop/neblio-qt
reddcoinqt=/home/pi/reddcoin-2.0.1.2/reddcoin-qt

if [ -e "$neblioqt" ]; then
    echo "neblio installed....checking config file"
    neblio=/home/pi/.neblio/neblio.conf
    if [ -e "$neblio" ]; then
        echo "Config file already exists at $neblio"
    else
        echo "File does not exist"
        touch $neblio
        echo "neblio.conf file created"
        echo "rpcpassword=$RPCPASSWORD" >> $neblio
        echo "rpcuser=nebliorpc" >> $neblio
        echo "rpcport=8332" >> $neblio
        echo "rpcallowip=127.0.0.1" >> $neblio
        echo "configuration settings appended"
    fi
else
    echo "neblio not installed on this StakeBox"

fi

if [ -e "$reddcoinqt" ]; then
    echo "reddcoin installed....checking config file"
    reddcoin=/home/pi/.reddcoin/reddcoin.conf
    if [ -e "$reddcoin" ]; then
        echo "Config file already exists at $reddcoin"
    else
        echo "File does not exist"
        touch $reddcoin
        echo "reddcoin.conf file created"
        echo "rpcpassword=$RPCPASSWORD" >> $reddcoin
        echo "rpcuser=reddcoinrpc" >> $reddcoin
        echo "rpcport=8332" >> $reddcoin
        echo "rpcallowip=127.0.0.1" >> $reddcoin
        echo "configuration settings appended"
    fi
else
    echo "reddcoin not installed on this StakeBox"

fi
