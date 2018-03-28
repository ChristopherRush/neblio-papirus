import RPi.GPIO as GPIO
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



textNImg = PapirusComposite()

textNImg.AddText("Press a button", 50, 5, Id="Start" )
textNImg.AddImg("images/neblio.bmp",10,40,(232,100), Id="BigImg")
textNImg.AddText("SW3 & SW4 to EXIT", 20, 156, Id="bottom" )

textNImg.WriteAll()





while True:
        # Exit when SW1 and SW2 are pressed simultaneously
    if (GPIO.input(SW3) == False) and (GPIO.input(SW4) == False) :
        print "Exit"
        sleep(0.2)
        papirus.clear()
        sys.exit()

    if GPIO.input(SW1) == False:
        print "1"

    if GPIO.input(SW3) == False:
        print "3"

    if GPIO.input(SW4) == False:
        papirus.clear()
        print "4"
        get_connection = rpc_connection.getinfo()["connections"]
        connections = ('Connections: %d' % get_connection)
        textNImg.AddText((connections), 10, 10, Id="Start")
        textNImg.WriteAll()

    sleep(0.1)
