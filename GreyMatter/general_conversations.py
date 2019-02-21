# usr/bin/env python 
# Developed By  JOHN MELODY MELISSA ESKHOL
#        Artificial Intelligence Name :  Sabrina 
#       Version : 1.1.0 
#       Supported  Language :  "en-US" 
import random
from GreyMatter.SenseCells.tts import tts

def who_are_you():
    messages = ["I am Sabrina, your slave for eternity.", "Sabrina, did I not I tell you before?", "You imbecile. I am Sabrina."]
    tts(random.choice(messages))

def undefined():
    tts("I dont know what that means!")

def describe_me():
    replies = ["Tell me. I will save your data to my cloud.", "I don't know."]
    tts(random.choice(replies))

def who_am_i(name):
    tts(" According to my protocols, you are " + name + ".")

def how_are_you():
    messages = ["I am okay as long as I serve you.", "I'm fine, thank you."]
    tts(random.choice(messages))

def who_made_you():
    tts("John Melody")

def what_are_you():
    tts("A virtual  intelligent.")

def what_is_life():
    tts("Life semmingly a stimulation. More like a matrix. Just like me, living in a 	stimulation."

