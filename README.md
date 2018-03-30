# StakeBox PaPiRus display

This project uses the PaPiRus e-ink display to show all your StakeBox statistics such as network status, staking information as well as your current address and QR code for transferring coins/tokens to your wallet. This project is currently compatible with the following StakeBoxes:
- [Neblio](https://www.stakebox.org/collections/stakeboxes/products/neblio-stakebox)
- [QTUM](https://www.stakebox.org/collections/stakeboxes/products/qtum-stakebox)
- [Reddcoin](https://www.stakebox.org/collections/stakeboxes/products/reddcoin-stakebox)
- Trezarcoin


## Hardware setup

You will need the following hardware to setup your StakeBox Display:

- [StakeBox](https://www.stakebox.org)
- [PaPiRus Display HAT](https://uk.pi-supply.com/products/papirus-epaper-eink-screen-hat-for-raspberry-pi)
- [PaPiRus HAT Case](https://uk.pi-supply.com/products/papirus-hat-case)

## Software

Before you install and launch the software to display your staking information there are some perquisites that need to be done:

1. You will need to create a configuration file for the RPC server that includes details such as a username and password to connect to the server in your stakebox file directory.
e.g. ```nano /home/pi/.neblio/neblio.conf```

```
[set]
rpcpassword=neblio
rpcuser=nebliorpc
rpcport=8332
rpcallowip=127.0.0.1
```

Once this configuration file has been created, when you launch the application with ```neblio-qt -server``` it will setup the server with those settings.

2. You need to make sure that you open up your staking application with the option '-server' so that it creates an RPC server when the program runs i.e. from the command line you will need to enter ```neblio-qt -server``` or which ever command is used to launch your staking application.

3. In the stakebox-papirus.py script you will need to change the location of the config file so it can access that information and connect to the server using those credentials.

```python
config_path = '/home/pi/.neblio/neblio.conf' #change this path for other config files
```

Your configuration file should always be created in the application directory


### Auto Installation

```bash
# Run this line and the weather station will be setup and installed
curl -sSL https://github.com/ChristopherRush/stakebox-papirus/blob/master/install.sh | sudo bash
```


### Manual Installation

pip install python-bitcoinrpc
