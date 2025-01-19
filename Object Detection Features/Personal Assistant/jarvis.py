from cgitb import text
from datetime import date, datetime
from operator import index
from re import search
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser 
import os
import smtplib
import warnings
from gtts import gTTS
import playsound
import calendar

warnings.filterwarnings("ignore")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('rate',250)
engine.setProperty('voice', voices[0].id )
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.runAndWait()

def wishMe():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir ")
    speak("I am JARVIS. Please tell me how may I help you")
def takeCommand():
    #it takes input from user in form as speech
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)
    except Exception as e:
        print("Say that again please..")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.logic('varshith4152@gmail.com','Rithu@0809')
    server.sendmail('varshith4152@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching..')
            query = query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)    

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
        elif 'play music' in query:
            music_dir= 'C:\\Users\\varsh\\OneDrive\\Desktop\\Rithu\\music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code or VS code' in query:
            codePath= "C:\\Users\\varsh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'pictures' in query:
            codePath= "C:\\Users\\varsh\\OneDrive\\Desktop\\Rithu\\Pics"
            os.startfile(codePath)
        elif 'send email' in query:
            try:
                speak("What is the content")
                content = takeCommand()
                to = ""
                sendEmail(to,content)
                speak("sent successfully")
            except Exception as e:
                print(e)
                speak("I wasnt able to send due to issue")
        elif 'who are you' in query or "define yourself" in query:
                speak("Hello. I am jarvis. I am designed to assist you")
        elif 'your name' in  query:
            speak('my name is jarvis')
        elif 'how are you' in query:
            speak('I am doing okay sir')
            speak('\n What about you?' )
        elif 'good' in query:
            speak('Good to know sir')
        elif 'bad' in query:
            speak('Is there anything I can help you with? Wanna help a joke?')
        elif 'yes' in query or 'joke' in query:
            speak("Why can't you tell a window a joke? ........ It could crack up. ")
        elif 'another joke' in query:
            speak('Why did the math textbook visit the guidance counselor? It neede help figuring out its problems')
        #elif "open" in query():
         #   if "chrome" in query():
          #      speak= speak + "Opening Google Chrome"
           #     os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
            #elif "youtube" in text.lower():
             #   speak = speak + "Opening youtube"
              #  webbrowser.open("https://youtube.com/")
            #elif "google" in text.lower():
             #   speak = speak + "Opening google"
              #  webbrowser.open("http://www.google.com/")
            
        #elif 'youtube' in text.lower():
            #ind = text.lower().split(),index("youtube")
            #search = text.split()[ind + 1:]
            #webbrowser.open("https://www.youtube.com/results?search_query=" + "+".join(search))
            #speak = speak + "Opening" + str(search) + "on youtube"
        #elif "search" in text.lower():
            #ind = text.lower().split().index("search")
            #search = text.split()[ind + 1:]
            #webbrowser.open("https://www.google.com/search?q=" + "+".join(search))
            #speak = speak + "Searching" + str(search) + "on google"
        #elif "google" in text.lower():
            #ind = text.lower().split().index("google")
            #search = text.lower()[ind + 1:]
            #webbrowser.open("https://www.google.com/search?q=" + "+".join(search))
            #speak = speak + "Searching" + str(search) + " on google"
def today_date(): 
    now = datetime.now()
    date_now = datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    ordinals = ["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th","15th","16th","17th","18th","19th","20th","21st","22nd","23rd","24th","25th","26th","27th","28th","29th","30th","31th"]
    return f'Today is {week_now}, {months[month_now -1]} the {ordinals[day_hour -1]}.'
       # elif 'order me pizza' in query:
def response(text):
    print(text)
    tts=gTTS(text=text, lang="en")
    audio = "Audio.mp3"
    tts.save(audio)
    playsound.playsound(audio)
    os.remove(audio)

def call(text):
    action_call= "jarvis"
    text = text.lower()
    if action_call in text:
        return True
    return False
