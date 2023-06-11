import pyttsx3
import os
import speech_recognition as sr
import time,pyautogui,win32gui,win32con
import setproctitle


# Your script code goes here
# ...

def minimize_terminal_window():
    # Find the Python terminal window by its title
    t="C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.1264.0_x64__qbz5n2kfra8p0\python3.11.exe"
    hwnd = win32gui.FindWindow(None, t)  # Replace "Python" with the actual title of your terminal window

    # Minimize the window
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
    
def text_to_type(text):
    pyautogui.typewrite(text)
def say_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source,phrase_time_limit=5)
        print("Time over, thanks")
    try:
        return r.recognize_google(audio)
    except:
        return "Sorry, I did not get that"
    



def main(terminal_name):
    while terminal_name is not None:
        print("Terminal Name:", terminal_name)
        # Example usage
        say_text("Hi Sir, say something.. or say quit...")
        while True:
            os.system('cls')
            text_to_say =  speech_to_text()  #input("Enter text to say: ")
            
            if text_to_say == 'quit' or text_to_say == 'exit' or text_to_say == 'bye':
                say_text("Bye Sir, Have a nice day")
                os.system('cls')
                exit()
            if text_to_say == 'clear':
                os.system('cls')
                continue
            elif 'type' in text_to_say:
                say_text("Typing "+text_to_say[5:])
                text_to_type(text_to_say[5:])
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
            elif 'open' in text_to_say or 'run' in text_to_say:
                os.system('cls')
                say_text("Opening "+text_to_say[5:])
                os.system("start "+text_to_say[5:])
                continue
            elif 'search' in text_to_say or 'find' in text_to_say:
                os.system('cls')
                say_text("Searching "+text_to_say[7:])
                os.system("start chrome https://www.google.com/search?q="+text_to_say[7:])
                continue
            elif 'play' in text_to_say:
                os.system('cls')
                say_text("Playing "+text_to_say[5:])
                os.system("start chrome https://www.youtube.com/results?search_query="+text_to_say[5:])
            elif 'weather' in text_to_say:
                os.system('cls')
                say_text("Showing weather report of "+text_to_say[8:])
                os.system("start chrome https://www.google.com/search?q="+text_to_say[8:]+"+weather")
            elif 'news' in text_to_say:
                os.system('cls')
                say_text("Showing news of "+text_to_say[5:])
                os.system("start chrome https://www.google.com/search?q="+text_to_say[5:]+"+news")
            elif 'map' in text_to_say:
                os.system('cls')
                say_text("Showing map of "+text_to_say[4:])
                os.system("start chrome https://www.google.com/maps/place/"+text_to_say[4:])
            elif 'close' in text_to_say or 'exit' in text_to_say or 'quit' in text_to_say:
                os.system('cls')
                say_text("Exiting "+text_to_say[5:])
                os.system(f"taskkill /F /IM {text_to_say[5:]}.exe")
            say_text(text_to_say)

minimize_terminal_window()
terminal_name = "speech_recognition_1.py"

main(terminal_name)