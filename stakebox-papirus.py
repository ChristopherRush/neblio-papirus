import RPi.GPIO as GPIO
import sys
import ConfigParser #used to parse config file
import os
import StringIO
#import wget

from papirus import Papirus
from time import sleep
from papirus import PapirusImage
from papirus import PapirusComposite
from bitcoinrpc.authproxy import AuthServiceProxy

nebliopath='/home/pi/.neblio/neblio.conf'
qtumpath=''
reddcoinpath='/home/pi/.reddcoin/reddcoin.conf'
trezarcoinpath=''

#Check with staking application is installed
if os.path.isfile(nebliopath):
    config_path = nebliopath
#    url = 'explorer.nebl.io/qr/%s' %address
    print "Neblio installed"
else:
    print "Neblio not installed"

if os.path.isfile(reddcoinpath):
    config_path = reddcoinpath
    print "Reddcoin installed"
else:
    print "Reddcoin not installed"

#Parse config file so you can read its values
with open(config_path, 'r') as f:
    a = '[config]\n' #Adds section header to the string. By default the staking app cannot read the config file if there is a section header
    b = f.read()
    config_string = a + b
buf = StringIO.StringIO(config_string) #Creates a buffer
config = ConfigParser.ConfigParser()
config.readfp(buf)

#Server RPC URL
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%((config.get('config','rpcuser')),(config.get('config','rpcpassword'))))

#Get server status must run xxxx-qt -server first
try:
    rpc_connection.getinfo()
    server_status = True
except:
    server_status = False
    pass

#Button GPIO pins
SW1 = 16
SW2 = 19
SW3 = 20
SW4 = 21


GPIO.setmode(GPIO.BCM) #Use BCM GPIO numbering

#Set GPIO pins as inputs
GPIO.setup(SW1, GPIO.IN)
GPIO.setup(SW2, GPIO.IN)
GPIO.setup(SW3, GPIO.IN)
GPIO.setup(SW4, GPIO.IN)


papirus = Papirus() #create papirus object
textNImg = PapirusComposite() #create variable to store image/text

#Boot image when started
if server_status == True:
    textNImg.AddText("Press a button", 50, 5, Id="Start" )
    textNImg.AddImg("images/StakeBox-Black.bmp",69,25,(125,125), Id="BigImg")
    textNImg.AddText("Server Status: Active ", 10, 156, Id="bottom")
else:
    textNImg.AddText("Press a button", 50, 5, Id="Start" )
    textNImg.AddImg("images/StakeBox-Black.bmp",69,25,(125,125), Id="BigImg")
    textNImg.AddText("Server Status: Down ", 10, 156, Id="bottom")
textNImg.WriteAll()


while True:
    if GPIO.input(SW1) == False:
        print "1"
        textNImg = PapirusComposite() #Clears the draw buffer

        getaddress = rpc_connection.getaccountaddress()[""]
        address = ('Address: %s' % getaddress)
        textNImg.AddText((address), 10, 10, Id="1")
        textNImg.WriteAll()
    if GPIO.input(SW3) == False:
        print "3"
        textNImg = PapirusComposite() #Clears the draw buffer
        #papirus.clear() #Clear the display

        #Get info from RPC connection
        get_staking = rpc_connection.getstakinginfo()["staking"]
        get_curr_block_size = rpc_connection.getstakinginfo()["currentblocksize"]
        get_curr_block_tx = rpc_connection.getstakinginfo()["currentblocktx"]
        get_pooledtx = rpc_connection.getstakinginfo()["pooledtx"]
        get_search = rpc_connection.getstakinginfo()["search-interval"]
        get_weight = rpc_connection.getstakinginfo()["weight"]
        get_netweight = rpc_connection.getstakinginfo()["netstakeweight"]
        get_exp_time = rpc_connection.getstakinginfo()["expectedtime"]

        #Append value to string
        staking = ('Staking: %s' % get_staking)
        currentblocksize = ('Block Size: %f' % get_curr_block_size)
        currentblocktx = ('Block Tx: %f' % get_curr_block_tx)
        pooledtx = ('PooledTx: %d' % get_pooledtx)
        search_int = ('Search: %d' % get_search)
        weight = ('Weight: %d' % get_weight)
        netweight = ('Net Weight: %d' % get_netweight)
        expectedtime = ('Expected: %f' % get_exp_time)

        #Write to the PaPiRus screen
        textNImg.AddText((staking), 10, 10, Id="1")
        textNImg.AddText((currentblocksize), 10, 30, Id="2")
        textNImg.AddText((currentblocktx), 10, 50, Id="3")
        textNImg.AddText((pooledtx), 10, 70, Id="4")
        textNImg.AddText((search_int), 10, 90, Id="5")
        textNImg.AddText((weight), 10, 110, Id="6")
        textNImg.AddText((netweight), 10, 130, Id="7")
        textNImg.AddText((expectedtime), 10, 150, Id="8")
        textNImg.WriteAll()

    if GPIO.input(SW4) == False:
        print "4"
        textNImg = PapirusComposite() #Clears the draw buffer
        #papirus.clear() #Clear the display


        get_version = rpc_connection.getinfo()["version"]
        get_balance = rpc_connection.getinfo()["balance"]
        get_stake = rpc_connection.getinfo()["stake"]
        get_connection = rpc_connection.getinfo()["connections"]
        get_blocks = rpc_connection.getinfo()["blocks"]
        get_pos = rpc_connection.getstakinginfo()["difficulty"]

        version = ('Version: %s' % get_version)
        balance = ('Balance: %f' % get_balance)
        stake = ('Stake: %f' % get_stake)
        connections = ('Connections: %d' % get_connection)
        blocks = ('Blocks: %d' % get_blocks)
        pos = ('PoS: %f' % get_pos)

        textNImg.AddText((version), 10, 10, Id="1")
        textNImg.AddText((balance), 10, 30, Id="2")
        textNImg.AddText((stake), 10, 50, Id="3")
        textNImg.AddText((connections), 10, 70, Id="4")
        textNImg.AddText((blocks), 10, 90, Id="5")
        textNImg.AddText("-----Difficulty-----", 10, 110, Id="6")
        textNImg.AddText((pos), 10, 130, Id="7")
        textNImg.WriteAll()

    sleep(0.1)
