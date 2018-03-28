import RPi.GPIO as GPIO
import sys

from papirus import Papirus
from time import sleep
from papirus import PapirusImage
from papirus import PapirusComposite
from bitcoinrpc.authproxy import AuthServiceProxy

rpc_connection = AuthServiceProxy("http://nebliorpc:Dtmqe2aj1Fc35nKMKMrwyCKEYxnatVGpW9tvXhuXdTHt@127.0.0.1:8332")

SW1 = 16
SW2 = 19
SW3 = 20
SW4 = 21


GPIO.setmode(GPIO.BCM)

GPIO.setup(SW1, GPIO.IN)
GPIO.setup(SW2, GPIO.IN)
GPIO.setup(SW3, GPIO.IN)
GPIO.setup(SW4, GPIO.IN)


papirus = Papirus()
textNImg = PapirusComposite()

textNImg.AddText("Press a button", 50, 5, Id="Start" )
textNImg.AddImg("images/neblio.bmp",10,40,(232,100), Id="BigImg")
textNImg.AddText("SW3 & SW4 to EXIT", 20, 156, Id="bottom" )

textNImg.WriteAll()





while True:
        # Exit when SW1 and SW2 are pressed simultaneously
    if (GPIO.input(SW3) == False) and (GPIO.input(SW4) == False) :
        print "Exit"
        papirus.clear()
        sleep(0.2)
        sys.exit()

    if GPIO.input(SW1) == False:
        print "1"

    if GPIO.input(SW3) == False:
        print "3"

    if GPIO.input(SW4) == False:

        print "4--"
        textNImg = PapirusComposite() #Clears the draw buffer
        papirus.clear() #Clear the display


        get_version = rpc_connection.getinfo()["version"]
        get_balance = rpc_connection.getinfo()["balance"]
        get_stake = rpc_connection.getinfo()["stake"]
        get_connection = rpc_connection.getinfo()["connections"]
        get_blocks = rpc_connection.getinfo()["blocks"]
        get_pos = rpc_connection.getinfo()["proofofstake"]

        version = ('Version: %s' % get_version)
        balance = ('Balance: %d' % get_balance)
        stake = ('Stake: %d' % get_stake)
        connections = ('Connections: %d' % get_connection)
        blocks = ('Blocks: %d' % get_blocks)
        pos = ('Proof-of-Stake: %d' % get_pos)

        textNImg.AddText((version), 10, 10, Id="1")
        textNImg.AddText((balance), 10, 30, Id="2")
        textNImg.AddText((stake), 10, 50, Id="3")
        textNImg.AddText((connections), 10, 70, Id="4")
        textNImg.AddText((blocks), 10, 90, Id="5")
        textNImg.AddText("-----Difficulty-----", 10, 110, Id="6")
        textNImg.AddText((pos), 10, 130, Id="7")
        textNImg.WriteAll()

    sleep(0.1)
