import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import ctypes

speech = sr.Recognizer()

#Connecting with window's engine for text to speech converter
try:
    engine = pyttsx3.init()
except ImportError:
    print("Requested Driver is not found")
except RuntimeError:
    print("Driver Failed to initialize")

voices = engine.getProperty('voices')

for voice in voices:
    print(voice.id)
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
rate = engine.getProperty('rate')
engine.setProperty('rate',rate)

#defining list and dictionary
greeting_dict = {'hello': 'hello', 'hi': 'hi'}
open_launch_dict = {'open':'open', 'launch':'launch'}
social_media_dict = {'facebook':'https://facebook.com/', 'twitter':'https://twitter.com/', 'youtube':'https://youtube.com/', 'linkedin':'https://linkedin.com/'}
google_searches_dict = {'what':'what','why':'why','who':'who','which':'which'}

#Defining Functions 
def speak_text_cmd(cmd):
    engine.say(cmd )
    engine.runAndWait()

def read_voice_cmd():
    voice_text = ''
    with sr.Microphone() as source:
        print('Speak...')
        audio = speech.listen(source=source,timeout=120,phrase_time_limit=5)
    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Network Error")
    return voice_text

def is_valid_note(greet_dict, voice_note):
    for key, value in greet_dict.items():
        try:
            if value==voice_note.split(' ')[0]:
                return True
                break
            elif key == voice_note.split(' ')[1]:
                return True
                break
        except IndexError:
            pass
    return False
def is_valid_google_search(phrase):
    if(google_searches_dict.get(phrase.split(' ')[0]) == phrase.split(' ')[0]):
        return True

#Main Function
if __name__ == '__main__':
    speak_text_cmd("Hello Mr. Pravin. This is Jarves as Your personal Assistant")
    
    while True:
        voice_note = read_voice_cmd().lower()
        print('cmd : {}'.format(voice_note))
        
        if is_valid_note(greeting_dict, voice_note):
            speak_text_cmd('Hello Sir, How Can i help you')
            continue
        elif 'how are you' in voice_note:
            speak_text_cmd('I am fine sir, Thank you for asking.')
            continue
        elif is_valid_google_search(voice_note):
            webbrowser.open('https://www.google.co.in/search?q={}'.format(voice_note))
            continue
        elif is_valid_note(open_launch_dict, voice_note):
            if is_valid_note(social_media_dict, voice_note):
                key = voice_note.split(' ')[1]
                webbrowser.open(social_media_dict.get(key))
            else:
                os.system('explorer C:\\{}'.format(voice_note.replace('open ','').replace('launch','')))
            continue
        #lock, shutdown or restart the system
        elif 'lock' in voice_note:
            for value in ['pc','system','windows','window','computer']:
                ctypes.windll.user32.LockWorkStation()
            continue
        elif 'shutdown' in voice_note:
            for value in ['pc','system','windows','window','computer']:
                os.system("shutdown /s /t 1")
            break
        elif 'restart' in voice_note:
            for value in ['pc','system','windows','window','computer']:
                os.system("shutdown /r /t 1")
            break
        #thank you or by command
        elif 'thank you' in voice_note:
            speak_text_cmd('Your most welcome, sir.')
            continue
        elif 'bye' in voice_note:
            speak_text_cmd("Bye sir, Have a good day.")
            break
        elif '' in voice_note:
            continue
        elif ' ' in voice_note:
            continue
        
            
