from papirus import PapirusComposite

# Calling PapirusComposite this way will mean nothing is written to the screen until WriteAll is called
textNImg = PapirusComposite()

# Write text to the screen at selected point, with an Id
# Nothing will show on the screen
textNImg.AddText("hello world", 10, 10, Id="Start" )


# Now display all elements on the screen
textNImg.WriteAll()
