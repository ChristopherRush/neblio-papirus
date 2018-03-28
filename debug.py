import RPi.GPIO as GPIO
from papirus import Papirus
from time import sleep
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

SW1 = 21
SW2 = 16
SW3 = 20
SW4 = 19
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
            write_text(papirus, "Exiting ...", SIZE)
            sleep(0.2)
            papirus.clear()
            sys.exit()

        if GPIO.input(SW1) == False:
            write_text(papirus, "One", SIZE)

        if GPIO.input(SW2) == False:
            write_text(papirus, "Two", SIZE)

        if GPIO.input(SW3) == False:
            write_text(papirus, "Three", SIZE)

        if GPIO.input(SW4) == False:
            write_text(papirus, "Four", SIZE)

        if (SW5 != -1) and (GPIO.input(SW5) == False):
            write_text(papirus, "Five", SIZE)

        sleep(0.1)

def write_text(papirus, text, size):

    # initially set all white background
    image = Image.new('1', papirus.size, WHITE)

    # prepare for drawing
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', size)

    # Calculate the max number of char to fit on line
    line_size = (papirus.width / (size*0.65))

    current_line = 0
    text_lines = [""]

    # Compute each line
    for word in text.split():
        # If there is space on line add the word to it
        if (len(text_lines[current_line]) + len(word)) < line_size:
            text_lines[current_line] += " " + word
        else:
            # No space left on line so move to next one
            text_lines.append("")
            current_line += 1
            text_lines[current_line] += " " + word

    current_line = 0
    for l in text_lines:
        current_line += 1
        draw.text( (0, ((size*current_line)-size)) , l, font=font, fill=BLACK)

    papirus.display(image)
    papirus.partial_update()
