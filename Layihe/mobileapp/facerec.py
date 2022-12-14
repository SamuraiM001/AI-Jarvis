# pip install pyttsx3 pypiwin32
import pyttsx3

# One time initialization
engine = pyttsx3.init("espeak")

# Set properties _before_ you add things to say
engine.setProperty('rate', 150)# Speed percent (can go over 100)
engine.setProperty('volume', 0.9)# Volume 0-1

# Queue up things to say.
# There will be a short break between each one
# when spoken, like a pause between sentences.
engine.say("You've got mail!")
engine.say("You can queue up multiple items")

# Flush the say() queue and play the audio
engine.runAndWait()

# Program will not continue execution until
# all speech is done talking
