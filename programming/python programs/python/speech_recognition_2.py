import pyttsx3
import os
import speech_recognition as sr
import subprocess
import time

def say_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source, phrase_time_limit=2)
        print("Time over, thanks")
    try:
        return r.recognize_google(audio)
    except:
        return "Sorry, I did not get that"

# Example usage
say_text("Hi Sir, say something... or say quit...")
while True:
    os.system('cls')
    text_to_say = speech_to_text()

    if text_to_say == 'quit' or text_to_say == 'exit' or text_to_say == 'bye':
        say_text("Bye Sir, Have a nice day")
        os.system('cls')
        exit()
    if text_to_say == 'clear':
        os.system('cls')
        continue
    elif text_to_say == 'time':
        os.system('time /t')
        say_text("Sir, current time is")
        text_to_say = time.strftime("%I:%M %p")
        continue
    elif text_to_say == 'date':
        os.system('date /t')
        say_text("Sir, current date is")
        text_to_say = time.strftime("%m/%d/%Y")
        continue
    elif text_to_say.startswith('open '):
        os.system('cls')
        app_name = text_to_say[5:]
        process = subprocess.Popen(['where', app_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        path = output.decode().strip()
        if path:
            say_text("Opening " + app_name)
            os.system("start " + path)
        else:
            say_text("Sorry, I couldn't find the application.")
        continue

    say_text(text_to_say)
