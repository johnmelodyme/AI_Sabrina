# usr/bin/env python 
# Developed By  JOHN MELODY MELISSA ESKHOL
#        Artificial Intelligence Name :  Sabrina 
#       Version : 1.1.0 
#       Supported  Language :  "en-US" 

from GreyMatter import tell_time, goodbye, general_conversations, location

def brain(name, speech_text):
    def check_message(check):
        words_of_message = speech_text.split() # split speech_text into words and store it in
                                               # words_of_message, which is an array of words
        if set(check).issubset(set(words_of_message)):
            return True
        else:
            return False

    if check_message(["who", "are", "you"]):
        general_conversations.who_are_you()
    elif check_message(["how", "i", "look"]) or check_message(["how", "am", "i"] or check_message(["describe", "me"])):
        general_conversations.describe_me()
    elif check_message(["who", "am", "i"]):
        general_conversations.who_am_i(name)
    elif check_message(["how", "are", "you"]):
        general_conversations.how_are_you()
    elif check_message(["time"]):
        tell_time.what_is_time()
    elif check_message(["say", "goodbye", "Sabrina"]):
        goodbye.goodbye()
    elif check_message(["who","made","you"]):
        general_conversations.who_made_you()
    elif check_message(["what","are","you"]):
        general_conversations.what_are_you()
    elif check_message(["location"]):
        general_conversations.where_am_i()
    elif check_message(["what","is","life"]):
	general_conversations.what_is_life()

    else:
        general_conversations.undefined()
