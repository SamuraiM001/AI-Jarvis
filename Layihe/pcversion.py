# version:1 21.10.2022 face recognition and have to get informations and animations
# version:2 decission making
# import modules
import datetime
import json
import random
import wikipedia
import smtplib
import ctypes
import subprocess  # subprocess module allows you to spawn new processes
import time
from unicodedata import name
import pygame
import cv2
import webbrowser
from pyowm import OWM
from pyowm.utils.config import get_default_config

# import face_recognition
from ast import Or
from winsound import (
    Beep,
)  # datetime module supplies classes for manipulating dates and times

import pyjokes

# importing the pyttsx3 library
import pyttsx3
import pywhatkit as kt
import requests

# master
import speech_recognition as sr  # speech_recognition Library for performing speech recognition with support for Google Speech Recognition, etc..
import sympy
from gtts import gTTS

# =======
from PIL import Image
from playsound import *  # for sound output
from playsound import playsound  # to play sounds
from pynput import keyboard
from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller

# for 30 seconds clip clip that and discord ctrl+k quick-move (might not come to fruition)


# pip install pyttsx3
# need to run only once to install the library
global nameofuser
global age

minrate = 100
currentrate=180
maxrate = 350
owm = OWM('edfe12ce94a5ee5318904f6cc2a2af73')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Баку')
w = observation.weather

# initialisation
language = "en"
wikipedia.set_lang(language)
ended = False
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", currentrate)
exit_assistant = False





class meta_human:
    def initialize():
        background_colour = (255, 255, 255)
        (width, height) = (1350, 700)
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("AI")
        screen.fill(background_colour)
        imp = pygame.image.load("C:\\Users\\ACER\\test.png").convert_alpha()
        screen.blit(imp, (250, 250))
        pygame.display.flip()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sayweather():
    
        speak("In Baku " + w.detailed_status)
        speak("Wind: " + str(w.wind()["speed"]) + " meters per second")
        speak("Temperature: " + str(w.temperature('celsius')["temp"]) + " celsius")
        speak("Humidity: " + str(w.humidity))
    
def play_game():

    speak("Which Game Do you want to play")
    speak("1 . Number Guessing game")
    speak("or 2 . Quiz game")
    speak("or 3 . Rock Paper scissors")
    speak("or 4 . Odd or Even")

    speak("If you want to leave say exit or leave anytime")

    G = takecommand()
    G = str(G)
    if (
        G.find("1") != -1
        or G.find("one") != -1
        or G.lower().find("1") != -1
        or G.find("first") != -1
        or G.find("number guessing") != -1
    ):
        speak("Which type of number guessing game you want to play ?")
        speak("1 . Number Guessing game from 1 - 1000")
        speak("2 . Number Guessing game from 1 - 100")
        speak("3 . Number Guessing game from 1 - 10")
        N = takecommand()
        N = str(N)
        if (
            N.find("1") != -1
            or N.find("one") != -1
            or N.find("number guessing 1") != -1
        ):
            speak("Ok")
            num = random.randint(1, 1000)
            print(num)
            speak("Try guessing random number")
            ans = takecommand()
            while ans != str(num):
                speak("Your Guess Is  Wrong . try again")
                ans = takecommand()
                if (
                    ans.find("bye") != -1
                    or ans.find("goodbye") != -1
                    or ans.find("exit") != -1
                    or ans.find("leave") != -1
                ):
                    return 0
            speak(
                "Cangrulations . You win .  Now return to my job .  How can i help you sir "
            )
            return 0
        elif (
            N.find("2") != -1
            or N.find("two") != -1
            or N.find("number guessing 2") != -1
        ):
            speak("Ok")
            num = random.randint(1, 100)
            print(num)
            speak("Try guessing random number")
            ans = takecommand()
            while ans != str(num):
                speak("Your Guess Is  Wrong . try again")
                ans = takecommand()
                if (
                    ans.find("bye") != -1
                    or ans.find("goodbye") != -1
                    or ans.find("exit") != -1
                    or ans.find("leave") != -1
                ):
                    return 0
            speak(
                "Cangrulations . You win .  Now return to my job .  How can i help you sir? "
            )
            return 0
        elif (
            N.find("3") != -1
            or N.find("three") != -1
            or N.find("number guessing 3") != -1
        ):
            speak("Ok")
            num = random.randint(1, 10)
            print(num)
            speak("Try guessing random number")
            ans = takecommand()
            while ans != str(num):
                speak("Your Guess Is  Wrong . try again")
                ans = takecommand()
                if (
                    ans.find("bye") != -1
                    or ans.find("goodbye") != -1
                    or ans.find("exit") != -1
                    or ans.find("leave") != -1
                ):
                    return 0
            speak(
                "Cangrulations . You win .  Now return to my job .  How can i help you sir "
            )
            return 0
        elif (
            N.find("bye") != -1
            or N.find("goodbye") != -1
            or N.find("leave") != -1
            or N.find("exit") != -1
        ):
            return N
        else:
            speak("There is No Game type Like That . Say it again ")
            N = takecommand()
    if (
        G.find("2") != -1
        or G.find("two") != -1
        or G.find("second") != -1
        or G.lower().find("2") != -1
        or G.find("quiz") != -1
    ):

        speak("In This game you has to get 3 points to win")

        randquestion1 = random.choice(
            ["What color is eiffel tower", "Which color is chocolate"]
        )
        speak(randquestion1)
        ans1 = takecommand()
        ans1 = str(ans1)
        if ans1.lower().find("brown") != -1:
            speak("You get that correct")

            randquestion2 = random.choice(
                [
                    "Can you drive car in america if you are 19",
                    "Can you drink alcohol in america if you are 22",
                ]
            )
            speak(randquestion2)
            ans2 = takecommand()
            ans2 = str(ans2)
            if ans2.lower().find("yes") != -1:
                speak("You get that correct")
                randquestion3 = random.choice(
                    [
                        "Can you buy a bugatti with 500000 dollars?",
                        "Can you build a site with assembly?",
                    ]
                )
                speak(randquestion3)
                ans3 = takecommand()
                ans3 = str(ans3)
                if ans3.lower().find("no") != -1:
                    speak(
                        "You get that correct . And you win this game. Congratulations"
                    )
                    return "You win"
                else:
                    speak("You get that wrong")
                    ans3 = takecommand()

            else:
                speak("You get that wrong")
                ans2 = takecommand()

        else:
            speak("You get that wrong")
            ans1 = takecommand()
    if (
        G.find("3") != -1
        or G.lower().find("three") != -1
        or G.lower().find("third game") != -1
        or G.lower().find("rock") != -1
        or G.lower().find("paper") != -1
        or G.lower().find("scissors") != -1
    ):
        computerwins = 0
        playerwins = 0
        ties = 0
        end = 0

        while True:

            choices = ["rock", "paper", "scissors"]

            speak("Rock, Paper, Scissors, or End")
            userChoice = takecommand()
            computerChoice = random.choice(choices)
            speak(computerChoice)

            if userChoice == computerChoice:
                time.sleep(0.5)
                speak("Tie!\n")
                ties += 1
                end += 1

            elif userChoice == "rock":
                if computerChoice == "paper":
                    time.sleep(0.5)
                    print("Computer Win!\n")
                    computerwins += 1
                    end += 1

                else:
                    time.sleep(0.5)
                    speak("You win!\n")
                    playerwins += 1
                    end += 1

            elif userChoice == "paper":
                if computerChoice == "rock":
                    time.sleep(0.5)
                    speak("You win!\n")
                    playerwins += 1
                    end += 1

                else:
                    time.sleep(0.5)
                    speak("I win!\n")
                    computerwins += 1
                    end += 1

            elif userChoice == "scissors":
                if computerChoice == "rock":
                    time.sleep(0.5)
                    speak("I win!")
                    computerwins += 1
                    end += 1

                else:
                    time.sleep(0.5)
                    speak("You win!")
                    playerwins += 1
                    end += 1

            elif userChoice == "end":
                choices.append("end")
                speak("Great game!")
                speak(f"Total score for Me:  {computerwins}  wins!")
                speak(f"Total score for You: {playerwins}  wins!")
                speak(f"Total ties:  {ties} ties!")
                time.sleep(2)
                break
    if (
        G.find("4") != -1
        or G.lower().find("four") != -1
        or G.lower().find("for") != -1
        or G.lower().find("odd") != -1
        or G.lower().find("even") != -1
        or G.lower().find("fourth") != -1
        or G.lower().find("4") != -1
    ):
        while True:
            num = random.randint(1, 1000)
            speak(
                "I have a number . Try to guest is this number an odd or even number."
            )
            if num % 2 == 0:
                guess = "odd"
            else:
                guess = "even"
            inptnum = takecommand()

            if inptnum.lower().find(guess) != -1:
                speak("Yes . You get it right . Do you want to continue")
                ans = takecommand()
                if ans.lower().find("yes") != -1:
                    speak("ok")

    elif (
        G.find("bye") != -1
        or G.find("goodbye") != -1
        or G.find("leave") != -1
        or G.find("exit") != -1
    ):
        speak("Ok")
        return None
    else:
        speak("There Is No Game Like That")
        return
    
    



# def recognize():
#     img = cv2.imread("./Murad2.jpeg")
#     img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#     img_encoding=face_recognition.face_encodings(img_rgb)[0]
#     frame =cv2.read()
#     result = face_recognition.compare_faces([img_encoding],frame)
#     print(result)
#     cv2.waitKey(0)


def wishme():
    # This function wishes user
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening !")
    speak("how can I help you")



def helpmentally():
   
    speak(random.choice(["Why . Tell me the reason", "Why are you trying to do it?",]))
    k = takecommand()
    if k.lower().find("money")!=-1:
        speak(
            random.choice(
                [
                    "Money is the material thing. Dont worry about it . It will be just fine . Live your life with your family members and always be happy",
                    "hey. buddy.. i  know this is  the last thing you want to see. but hear me out . when i was 11 people tell me to not be sad and to get over it. familiar words right? i wanted to die like you, but i couldnt cause of a few family members who would be sad if i died. i know im being egocentrism, but i just want to say that you're not alone and people have some same expeiriences. if you want to talk meet some new people . See some psychologist . it will help you .",
                ]
            )            
        )
        kt.search("Money Problems")
        speak(
            "I think you have you make better decisions in your life . Cause it happens only once and you dont know what will happen afterlife . Live your life like you want . Always know that there was a parents that cannot live without you"
        )
        return

    if k.lower().find("family")!=-1:
        speak(
            random.choice(
                [
                    "Never . Never . You have to know that they love you no matter how they treat you . You is the one guy on the earth that theey would give their lives for . Be carefull with you words and never say that again",
                    "hey. buddy.. i  know this is  the last thing you want to see. but hear me out . when i was 11 people tell me to not be sad and to get over it. familiar words right? i wanted to die like you, but i couldnt cause of a few family members who would be sad if i died. i know im being egocentrism, but i just want to say that you're not alone and people have some same expeiriences. if you want to talk meet some new people . See some psychologist . ill be glad to meet you, so ill see you later i geuss",
                    "Please dont do it . I have cookies ",
                ]
            )
        )
        kt.search("Family Problems")
        speak(
            "I think you have you make better decisions in your life . Cause it happens only once and you dont know what will happen afterlife . Live your life like you want . Always know that there was a parents that cannot live without you"
        )
        return


# obtain audio from the microphone
def takecommand():
    # it takes user's command and returns string output
    global query
    Beep(600, 150)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source)
        r.dynamic_energy_threshold = 150
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said {query}\n")
     
        
    except Exception as e:
        print(e)
        speak("Please Repeat it sir")
        query = "null"

    while query =="null":
        query = takecommand()     
        
    return query

    



# for audio output instead of print
def voice(p):
    myobj = gTTS(text=p, lang="en", slow=False)
    myobj.save("try.mp3")
    playsound("try.mp3")


# recognize speech using Google Speech Recognition


def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ["1", "2", "left", "right"]:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        print("Key pressed: " + k)
        return False  # stop listener; remove this if want more keys


# Run Application with Voice Command Function
# only_assistant
def on_release(key):
    print("{0} release".format(key))
    if key == Key.esc():
        # Stop listener
        return False


def get_app(Q):
    current = Controller()
    Q = str(Q)
    if (Q.lower().find("what time is it") != -1
        or Q.lower().find("tell me the time") != -1):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        speak(current_time)
    # mathematichs
    elif (
        Q.find("+") != -1
        or Q.find("-") != -1
        or Q.find("*") != -1
        or Q.find("**") != -1
        or Q.find("/") != -1
    ):
        speak(sympy.sympify(Q))
    # end
    # maners
    elif Q.lower().find("hello") != -1 or Q.lower().find("hi") != -1:
        speak(random.choice(["Hi sir", "Hello sir", "Welcome Sir"]))
    elif (
        Q.lower().find("i love you") != -1
    ):
        speak(random.choice(["Thank you sir . i love you too", "I know that you love me . Thats why i love you sir", "Thank you very much sir . I love that i had such a lovely user"]))
    elif (
        Q.lower().find("goodbye") != -1
        or Q.lower().find("dubai") != -1
        or Q.lower().find("leave") != -1
        or Q.lower().find("see you later") != -1
    ):
        speak(
            random.choice(
                [
                    "Wish You Luck Sir . Come again",
                    "Bye sir",
                    "Thank you for everything . GoodBye",
                ]
            )
        )
        exit()
    elif Q.lower().find("thank") != -1 or Q.lower().find("thanks") != -1:
        speak(random.choice(["Thank You too sir", "No problem", "Always for you sir"]))
    elif Q.lower().find("who") != -1 and Q.lower().find("are you") != -1:
        speak(
            random.choice(["Im AI.", "Im Artificcial intelegence.", "Im meta human."])
        )
        speak("I made by MRK studio")
    elif (
        Q.lower().find("what's your name") != -1
        or Q.lower().find("what is your name") != -1
        or Q.lower().find("who are you") != -1
        or Q.lower().find("who is you") != -1
        or Q.lower().find("your name") != -1
    ):
        speak(
            random.choice(["Im AI.", "Im Artificcial intelegence.", "Im meta human."])
        )
        speak("I made by MRK studio")
    elif ((Q.lower().find("set") != -1 and Q.lower().find("my") != -1) or Q.lower().find("name") != -1) or ((Q.lower().find("set") != -1 and Q.lower().find("my") != -1) or Q.lower().find("age") != -1) or ((Q.lower().find("set") != -1 and Q.lower().find("my") != -1) or Q.lower().find("data") != -1) or ((Q.lower().find("set") != -1 and Q.lower().find("my") != -1) or Q.lower().find("information") != -1) or ((Q.lower().find("set") != -1 and Q.lower().find("my") != -1) and Q.lower().find("info") != -1):
        speak("What is your name?")
        nameofuser=takecommand()
        speak("how old are you")
        age=takecommand()
        speak("Thank you sir. Lets continue")
    elif Q.lower().find("search")!=-1 or (Q.lower().find("how")!=-1 and Q.lower().find("to")!=-1)  or (Q.lower().find("how")!=-1 and Q.lower().find("can")!=-1) or (Q.lower().find("find")!=-1 and Q.lower().find("in")!=-1):
        results = wikipedia.summary(Q, sentences=3)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif Q.lower().find(
    "how are you") != -1 or Q.lower().find("how you feeling") != -1:
        speak(
            random.choice(["Very good,how are you sir?", "Thank you sir,i was  good"])
        )

    elif (
        Q.lower().find("how old are you") != -1
        or Q.lower().find("tell me your age") != -1
    ):
        speak(
            random.choice(
                ["I am old enough to be young", "I am old but my processor is young"]
            )
        )

    # end
    # Decission making
    elif (((
        Q.lower().find("i") != -1
        and Q.lower().find("want") != -1
        and Q.lower().find("kill") != -1
    ) or (Q.lower().find("die") != -1)) or
    (
        Q.lower().find("i") != -1
        and Q.lower().find("bored") != -1
        and Q.lower().find("life") != -1
    )):  
        helpmentally()
    # end-reg
    
    # program region
    # elif Q.lower().find("open notepad") != -1:
    #     subprocess.call(["Notepad.exe"])
    # elif Q.lower().find("open calculator") != -1:
    #     subprocess.call(["calc.exe"])
    # elif (
    #     Q.lower().find("open sticky note") != -1
    #     or Q.lower().find("open sticky notes") != -1
    # ):
    #     subprocess.call(["StikyNot.exe"])
    # elif Q.lower().find("open command prompt") != -1:
    #     subprocess.call(["cmd.exe"])
    # end
    # playing games
    elif Q.lower().find("play") != -1 and Q.lower().find("game") != -1:
        play_game()
    # end
    # site region
    elif "open YouTube" in Q:
        speak("Here you go to Youtube\n")
        webbrowser.open("https://youtube.com/")

    elif Q.lower().find("open google") != -1:
        speak("Here you go to Google\n")
        webbrowser.open("https://google.com/")

    elif Q.lower().find("open stackoverflow") != -1:
        speak("Here you go to Stack Over flow.Happy coding")
        webbrowser.open("https://stackoverflow.com/")

    # end

    # master
    

    elif Q.lower().find("tell") != -1 and Q.lower().find("joke") != -1:
        speak(pyjokes.get_joke())

    elif Q.lower().find("start recording") != -1:
        current.add("Win", "Alt", "r")
        speak("Started recording. just say stop recording to stop.")

    elif Q.lower().find("stop recording") != -1:
        current.add("Win", "Alt", "r")
        speak("Stopped recording. check your game bar folder for the video")

    elif Q.lower().find("clip that") != -1:
        current.add("Win", "Alt", "g")
        speak("Clipped. check you game bar file for the video")
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

    elif (Q.lower().find("how")!=-1 and Q.lower().find("weather") != -1) or (Q.lower().find("weather") != -1 and Q.lower().find("today") != -1):
        sayweather()
    elif Q.lower().find("lock device")!=-1:
        ctypes.windll.user32.LockWorkStation()
    elif (Q.lower().find("where is")!=-1 and Q.lower().find("located")!=-1) :
        Q=Q.replace("where is","")
        location=Q.replace("located","")            
        kt.search(location)
    elif   Q.lower().find("located")!=-1 :
        location=Q.replace("located","")
        kt.search(location)
    elif Q.lower().find("where is")!=-1:
        location =Q.replace("where is","")
        kt.search(location)

    else:
            speak(
                "Do you want me to search about it?"
            )
            an = takecommand()
            an = str(an)
            if (
                an.find("Yes") != -1
                or an.find("yes") != -1
                or an.find("yep") != -1
                or an.find("Yeah") != -1
            ):
                kt.search(Q)
                speak("i find  something in google about it")
            elif (
                an.find("nah") != -1
                or an.find("don't") != -1
                or an.find("no") != -1
                or an.find("nope") != -1
            ):
                speak("Ok .")
                return an
            else:
                return
       
    # master

    apps = {
        "time": datetime.datetime.now(),
        "notepad": "Notepad.exe",
        "calculator": "calc.exe",
        "stikynot": "StikyNot.exe",
        "shell": "powershell.exe",
        "paint": "mspaint.exe",
        "cmd": "cmd.exe",
        "browser": "C:\\Program Files\Internet Explorer\iexplore.exe",
        "vscode": "C:\\Users\\Users\\User\\AppData\\Local\\Programs\Microsoft VS Code",
    }
    # master

# Call get_app(Query) Func.

#exit_assistant = True
if __name__ == "__main__":
    meta_human.initialize()
    wishme()
    while not exit_assistant:
        Query = takecommand()
        get_app(Query)
    exit_assistant = True

# #include <stdio.h>

# int main() {
#     int n,k;
#     scanf("%d",&n);
#     while (n)
#     {
#         k=n%10;
#         n/=10;
#         if((k==7) && (n%10 == 3))
#         {
#             printf("Yes");
#             break;
#         }

#         printf("No");
#         break;


#     }
#     return 0;
# }
# #

# n=input("n=")
# s = set()
# for i in range(len(n)):
#     s.add(n[i])
# if len(n)==len(s):
#     print("no")
# else:
#     print("yes")
    