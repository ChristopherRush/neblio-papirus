from papirus import PapirusTextPos
from time import sleep
from papirus import Papirus
while True:
# Same as calling "PapirusTextPos(True [,rotation = rot])"
    text = PapirusTextPos(False)

# Write text to the screen at selected point, with an Id
# "hello world" will appear on the screen at (10, 10), font size 20, straight away
    text.AddText("hello world", 10, 10, Id="Start" )

# Add another line of text, at the default location
# "Another line" will appear on screen at (0, 0), font size 20, straight away
    text.AddText("Another line", Id="Top")

    text.update()
# Update the first line
# "hello world" will disappear and "New Text" will be displayed straight away
    text.UpdateText("Start", "hello world 1")
    text.partial_update()
# Remove The second line of text
# "Another line" will be removed from the screen straight away


# Clear all text from the screen
# This does a full update so is a little slower than just removing the text.
    text.Clear()
    sleep 1
