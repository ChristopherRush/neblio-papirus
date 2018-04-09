from __future__ import print_function

import os
import sys

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from datetime import datetime
import time
from papirus import Papirus

# Check EPD_SIZE is defined
EPD_SIZE=0.0
if os.path.exists('/etc/default/epd-fuse'):
    exec(open('/etc/default/epd-fuse').read())
if EPD_SIZE == 0.0:
    print("Please select your screen size by running 'papirus-config'.")
    sys.exit()

# Running as root only needed for older Raspbians without /dev/gpiomem
if not (os.path.exists('/dev/gpiomem') and os.access('/dev/gpiomem', os.R_OK | os.W_OK)):
    user = os.getuid()
    if user != 0:
        print("Please run script as root")
        sys.exit()

WHITE = 1
BLACK = 0

CLOCK_FONT_FILE = '/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf'
DATE_FONT_FILE  = '/usr/share/fonts/truetype/freefont/FreeMono.ttf'

def main(argv):

    """main program - draw and display time and date"""

    papirus = Papirus(rotation = int(argv[0]) if len(sys.argv) > 1 else 0)


    papirus.clear()

    demo(papirus)


def demo(papirus):
    """simple partial update demo - draw a clock"""

    # initially set all white background
    image = Image.new('1', papirus.size, WHITE)

    # prepare for drawing
    draw = ImageDraw.Draw(image)
    width, height = image.size

    clock_font_size = int((width - 4)/(8*0.65))      # 8 chars HH:MM:SS
    clock_font = ImageFont.truetype(CLOCK_FONT_FILE, clock_font_size)
    date_font_size = int((width - 10)/(10*0.65))     # 10 chars YYYY-MM-DD
    date_font = ImageFont.truetype(DATE_FONT_FILE, date_font_size)

    # clear the display buffer
    draw.rectangle((0, 0, width, height), fill=WHITE, outline=WHITE)
    previous_second = 0
    previous_day = 0

    value = 0
    while True:

        draw.rectangle((5, 10, width - 5, 10 + clock_font_size), fill=WHITE, outline=WHITE)

        draw.text((5, 10), "Hello world %d" % value, fill=BLACK, font=clock_font)

        papirus.partial_update()
        value += 1

# main
if "__main__" == __name__:
    if len(sys.argv) < 1:
        sys.exit('usage: {p:s}'.format(p=sys.argv[0]))

    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        sys.exit('interrupted')
        pass
