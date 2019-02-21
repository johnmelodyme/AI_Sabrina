import os

def tts(message):
# This function takes a message as an argument and converts it to speech depending
# on the OS.
    tts_engine = 'say'
    return os.system(tts_engine + ' ' + message)
