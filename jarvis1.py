import speech_recognition as sr
import os
import webbrowser
import openai
import datetime

from openai import audio
from wikipedia import languages


def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Pycharm')
    say("Hello boss I am Friday A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https//www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say("Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # if "open music" in query:
        #     musicPath = "/Users/pabitradas/Downloads/Kun Faaya Kun - Rockstar.mp3"
        #     os.system(f"open{musicPath}")

            if "the time" in query:
                hour = datetime.datetime.now().strftime("%H")
                min = datetime.datetime.now().strftime("%M")
                say(f"Sir the time is {hour} hour and {min} minutes")

            if "open facetime".lower() in query.lower():
                os.system(f"open /System/Applications/FaceTime.app")

            if "open safari".lower() in query.lower():
                os.system(f"open /System/Volumes/Preboot/Cryptexes/App/System/Applications/Safari.app")

            if "open Chat GPT".lower() in query.lower():
                os.system(f"open /Applications/ChatGPT.app")

            