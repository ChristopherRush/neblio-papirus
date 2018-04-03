#!/usr/bin/env bash

sudo apt-get update

sudo apt-get install pip, git

pip install python-bitcoinrpc

git clone https://github.com/ChristopherRush/stakebox-papirus.git

neblio=/home/pi/.neblio/neblio.conf
if [ -e "$neblio" ]; then
    touch $neblio
    "neblio.conf file created"
    echo "[config]" >> $neblio
    echo "rpcpassword=neblio" >> $neblio
    echo "rpcuser=nebliorpc" >> $neblio
    echo "rpcport=8332" >> $neblio
    echo "rpcallowip=127.0.0.1" >> $neblio
    echo "configuration settigns appended"
else
    echo "File does not exist"
fi
