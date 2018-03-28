import RPi.GPIO as GPIO
from papirus import Papirus
from time import sleep
from papirus import PapirusImage
from papirus import PapirusComposite

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

textNImg.AddText("Press a button", 20, 5, Id="Start" )
textNImg.AddImg("images/neblio.bmp",20,20, Id="BigImg")
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
        print "4"

    sleep(0.1)
