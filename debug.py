import RPi.GPIO as GPIO
from papirus import Papirus
from time import sleep
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

SW1 = 16
SW2 = 19
SW3 = 20
SW4 = 21
SW5 = 26

WHITE = 1
BLACK = 0

SIZE = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(SW1, GPIO.IN)
GPIO.setup(SW2, GPIO.IN)
GPIO.setup(SW3, GPIO.IN)
GPIO.setup(SW4, GPIO.IN)

while True:
        # Exit when SW1 and SW2 are pressed simultaneously
    if (GPIO.input(SW1) == False) and (GPIO.input(SW2) == False) :
        print "Exit"
        sleep(0.2)
        papirus.clear()
        sys.exit()

    if GPIO.input(SW1) == False:
        print "1"

    if GPIO.input(SW2) == False:
        print "2"

    if GPIO.input(SW3) == False:
        print "3"

    if GPIO.input(SW4) == False:
        print "4"

    sleep(0.1)
