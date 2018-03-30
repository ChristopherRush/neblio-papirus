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

1. You need to make sure that you open up your staking application with the option '-server' so that it creates an RPC server when the program runs i.e. from the command line you will need to enter ```neblio-qt -server```

### Auto Installation

### Manual Installation

pip install python-bitcoinrpc
