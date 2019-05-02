import speech_recognition as sr

from time import ctime
from time import os

from gtts import gTTs

import pyglet

import subprocess

def speak(audiosString):
    print(audiosString)
    tts=gTTs(text=audiosString,lang='en')
    tts.save("audio.mp3")


    wmp= r "C:\Program Files (x86)\Windows Media Player\wmplayer.exe"
        media_file=os.path.abspath/(os.path.realpath("Desktop\text.txt"))
        p=subprocess.call(wmp,media_file)

def recordAudio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say somthings:")
        audio=r.listen(source)
    data=""


    try:
        data=r.recognize_goole(audio)
        print("You said:",data)
        except sr.UnknownvalueError:
            print("Couldn't understand audio")
        except sr.RequestError as e:
            print("could not request result;{0}".format(e))



        return data
        def stan(data):
            if "How are you " in data:
                speak("i am fine thanks for asking")

        time.sleep(2)
        speak("What i can do for you?")


        while True:
            data=recordAudio()
