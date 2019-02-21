# usr/bin/env python 
# Developed By  JOHN MELODY MELISSA ESKHOL
#        Artificial Intelligence Name :  Sabrina 
#       Version : 1.1.0 
#       Supported  Language :  "en-US" 
#       "Main File"
import speech_recognition as sr     #  sudo apt install python3-pip && sudo pip3 install SpeechRecognition  
import yaml
from brain import brain
from GreyMatter.SenseCells.tts import tts

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

# Functioning Variables
name = profile_data['name']
city_name = profile_data['city_name']
tts('Welcome ' + name + ', systems are now ready to run. How can I help you?')

def main():
    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        # Things to ask Sabrina
        # Describe me. How am I? How do I look?
        # Who am I?
        # How are you?
        # What is the time?

        try:
            speech_text = r.recognize_google(audio).lower().replace("'", "")
            print("Sabrina thinks you said '" + speech_text + "'")
        except sr.UnknownValueError:
            print("Sabrina could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        brain(name, speech_text)

main()
