import re
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import pywhatkit
print('Initializing Shadow')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
MASTER = "Rejo"

# speak funtcion will speak the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()


# this fucnction will wish you as per the current time

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning"+MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon"+MASTER)
    else:
        speak("Good Night"+MASTER)
wishMe()
speak("I'm Shadow .How may i help you ?")

# main program starts here
# this function will take command from microphone

r = sr.Recognizer()


def main():
    with sr.Microphone() as source :
        r.adjust_for_ambient_noise(source)
        speak("Listening...")
        audio = r.listen(source)

        try :
            print("Recognizing...")
            transcript = r.recognize_google(audio)
            print("You Said : " + transcript)
        except :
            pass


# Logic for executing tasks as per the query
    if 'wikipedia' in transcript.lower():
        speak('Searching wikipedia...')
        transcript = transcript.replace("wikipedia", "")
        results = wikipedia.summary(transcript, sentences=2)
        print(results)
        speak(results)
    elif 'open youtube' in transcript.lower():
        webbrowser.open("youtube.com")
    elif 'open google' in transcript.lower():
        webbrowser.open("google.com")
    elif 'the time' in transcript.lower():
        strTime = datetime.datetime.now().strftime('%I:%M:%p')
        print(strTime)
        speak(f"{MASTER} the time is {strTime}")
    elif 'open code' in transcript.lower():
        codePath = "C:\Program Files\Microsoft VS Code\Code.exe"
        os.startfile(codePath)
    elif 'play' in transcript.lower():
        song = transcript.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)

main()
