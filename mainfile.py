import datetime
import time
import webbrowser
import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import os
import pyautogui
import random
from plyer import notification
from pygame import mixer
import speedtest
import os
import wikipedia
import translate


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


for i in range(3):
    user_pw = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt", "r")
    stored_pw = pw_file.read()
    pw_file.close()

    if user_pw == stored_pw:
        speak("WELCOME SIR! SAY [WAKE UP] TO START ME")
        print("WELCOME SIR! SAY [WAKE UP] TO START ME")
        break

    elif i == 2 and user_pw != stored_pw:
        exit()

    elif user_pw != stored_pw:
        print("Try Again")

from INTRO import play_gif
play_gif

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")

    except Exception as e:
        print("Say that again")
        return "None"
    return query


def alarm(query):
    timehere = open("03", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


def remember(reminder):
    with open("reminders.txt", "a") as file:
        file.write(reminder + "\n")
    speak("I will remember that.")


def recall():
    try:
        with open("reminders.txt", "r") as file:
            reminders = file.readlines()
        if reminders:
            speak("You asked me to remember the following:")
            for reminder in reminders:
                speak(reminder.strip())
        else:
            speak("You have no reminders.")
    except FileNotFoundError:
        speak("You have no reminders.")


def clear_memory():
    with open("reminders.txt", "w") as file:
        pass
    speak("Memory cleared.")


if __name__ == "__main__":

    while True:
        query = takeCommand().lower()

        if "wake up" in query:

            from greetME import greetMe

            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir, You can call me anytime")
                    break

                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt", "w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is {new_pw}")

                elif "schedule my day" in query:
                    tasks = []  # Empty list
                    speak("Do you want to clear old tasks (Please speak YES or NO)")
                    query = takeCommand().lower()

                    if "yes" in query:
                        file = open("tasks.txt", "w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the number of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i + 1}. {tasks[i]}\n")
                            file.close()

                    elif "no" in query:
                        no_tasks = int(input("Enter the number of tasks :- "))

                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i + 1}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                    file = open("tasks.txt", "r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title="My schedule :-",
                        message=content,
                        timeout=15
                    )

                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO] "))

                    if a == 1:
                        speak("Entering the focus mode....")
                        print("Entering the focus mode....")
                        os.startfile("D:\\user\\Downloads\\hackaivs\\www\\focusmode.py")
                        exit()

                    else:
                        pass

                #elif "show my focus" in query:
                #   from FocusGraph import focus_graph

                #    focus_graph()

                elif "translate" in query:
                    from trans import translategl

                    query = query.replace("jarvis", "")
                    query = query.replace("translate", "")
                    translategl(query)

                elif "open" in query:
                    query = query.replace("open", "")
                    query = query.replace("jarvis", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")

                elif "internet speed" in query:
                    wifi = speedtest.speedtest()
                    upload_net = wifi.upload()/1048576  # Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ", download_net)
                    speak(f"Wifi download speed is {download_net} Mbps")
                    speak(f"Wifi Upload speed is {upload_net} Mbps")

                elif "play a game" in query:
                    from game import game_play

                    game_play()

                elif "screenshot" in query:
                    try:
                        im = pyautogui.screenshot()
                        im.save("ss.jpg")
                        speak("Screenshot taken and saved as ss.jpg")
                    except Exception as e:
                        speak(f"An error occurred while taking a screenshot: {e}")

                elif "photo" in query:
                    try:
                        pyautogui.press("win")  # 'super' key for Windows, 'win' is more common in scripts
                        pyautogui.typewrite("camera")
                        pyautogui.press("enter")
                        time.sleep(2)  # Using time.sleep for better readability
                        speak("SMILE")
                        pyautogui.press("enter")
                        speak("Photo taken")
                    except Exception as e:
                        speak(f"An error occurred while taking a photo: {e}")

                elif "hello" in query:
                    speak("Hello sir, how are you?")
                    print("Hello sir, how are you?")

                elif "what can you do" in query or "perform" in query:
                    speak("limited system tasks you command me")
                    print("limited system tasks you command me")

                elif "i am fine" in query:
                    speak("That's great, sir")
                    print("That's great, sir")

                elif "how are you" in query or "how r y" in query:
                    speak("Perfect, sir")
                    print("Perfect, sir")

                elif "thank you" in query:
                    speak("You are welcome, sir")
                    print("You are welcome, sir")
                
                elif "My file music" in query:
                    music='c:\\Users\\muzza_ojzqw4t\\Music'
                    songs=os.listdir(music)
                    print(songs)
                    os.startfile(os.path.join(music,songs[0]))

                elif "playlist" in query:
                    a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
                    b = random.choice(a)

                    if b == 1:
                        webbrowser.open("https://www.youtube.com/watch?v=E-jmyhn-rm4")

                    elif b == 2:
                        webbrowser.open("https://www.youtube.com/watch?v=HFHl_tXSyaE")

                    elif b == 3:
                        webbrowser.open("https://www.youtube.com/watch?v=uWRlisQu4fo")

                    elif b == 4:
                        webbrowser.open("https://www.youtube.com/watch?v=jOTeBVtlnXU")

                    elif b == 5:
                        webbrowser.open("https://www.youtube.com/watch?v=dhYOPzcsbGM")

                    elif b == 6:
                        webbrowser.open("https://www.youtube.com/watch?v=qP-7GNoDJ5c")

                    elif b == 7:
                        webbrowser.open("https://www.youtube.com/watch?v=5r3B7yz6J68")

                    elif b == 8:
                        webbrowser.open("https://www.youtube.com/watch?v=5r3B7yz6J68")

                    elif b == 9:
                        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

                    elif b == 10:
                        webbrowser.open("https://www.youtube.com/watch?v=fPO76Jlnz6c")

                elif "pause the video" in query:
                    pyautogui.press("k")
                    speak("Video paused")

                elif "play the video" in query:
                    pyautogui.press("k")
                    speak("Video played")

                elif "mute the video" in query:
                    pyautogui.press("m")
                    speak("Video muted")

                elif "unmute the video" in query:
                    pyautogui.press("m")
                    speak("Video unmuted")

                elif "volume up" in query:
                    from volume_downorup import volumeup

                    speak("Turning volume up, boss")
                    volumeup()

                elif "volume down" in query:
                    from volume_downorup import volumedown

                    speak("Turning volume down, boss")
                    volumedown()

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif'search on wikipedia' in query:
                    speak('searching on wikipedia')
                    query=query.replace("wikipedia","")
                    result=wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    print(result)
                    speak(result)

                elif "open youtube" in query:
                    webbrowser.open("youtube.com")
                    #from SearchNow import searchYoutube

                    #searchYoutube(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia

                    searchWikipedia(query)

                elif "news" in query:
                    from News import latestnews

                    latestnews()

                elif "calculate" in query:
                    from calci import WolfRamAlpha
                    from calci import Calc

                    query = query.replace("calculate", "")
                    query = query.replace("jarvis", "")
                    Calc(query)

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage

                    sendMessage()

                elif "temperature" in query or "weather" in query:
                    search = "temperature in hyderabad"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"Current {search} is {temp}")

                elif "set an alarm" in query or "set a alarm" in query or "set alarm" in query or "alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    a = input("Please tell the time :- ")
                    speak("Set the time")
                    alarm(a)
                    speak("Done,sir")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")

                elif "offline" in query:
                    speak("Ok sir, You can call me anytime")
                    speak("Going to sleep, sir")
                    exit()

                elif "remember that" in query:
                    reminder = query.replace("remember that", "").replace("jarvis", "").strip()
                    remember(reminder)
                    print("I'll remember that you need to", reminder)

                elif "what do you remember" in query:
                    recall()

                elif "clear memory" in query:
                    clear_memory()

                elif "shutdown system" in query:
                    speak("Are you sure you want to shutdown?")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no): ").strip().lower()

                    while shutdown not in ["yes", "no"]:
                        speak("Invalid response. Please answer with 'yes' or 'no'.")
                        shutdown = input("Do you wish to shutdown your computer? (yes/no): ").strip().lower()

                    if shutdown == "yes":
                        speak("Shutting down the system.")
                        os.system("shutdown /s /t 1")
                    else:
                        speak("Shutdown canceled.")
