from decouple import config
from datetime import datetime
import pyttsx3

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

#Speech engine start
engine = pyttsx3.init('espeak')

#Set Rate
engine.setProperty('rate', 140)

#Set Volume
engine.setProperty('volume', 1)

#Set Voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[63].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.now().hour

    if (hour >= 6) and (hour < 12):
        speak(f'Bom dia {USERNAME}!')
    elif (hour >= 12) and (hour < 18):
        speak(f'Boa tarde {USERNAME}!')
    else:
        speak(f'Boa noite {USERNAME}')

    speak(f'Eu sou o {BOTNAME}. Como vai você? Esta é minha primeira apresentação em público e sou muito tímido. Perdoe meu jeito retraído.')

greet_user()