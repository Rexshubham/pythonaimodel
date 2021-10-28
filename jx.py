import  pyttsx3
import datetime
import  requests
from requests import get
import speech_recognition as sr
import wolframalpha
import random
import webbrowser
import pywhatkit as kit
import  os
import pyjokes
import wikipedia
import sys
import joke
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)  # setting up new voice rate
engine.setProperty('voices', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            speak("Recognizing...")
            query = r.recognize_google(audio)  # Using google for voice recognition.
            print(f"User said: {query}\n")  # User query will be printed.

        except Exception as e:
            # print(e)0
            print("Say that again please...")  # Say that again will be printed in case of improper voice
            speak("Say that again please...")
            return "None"  # None string will be returned




        return query
def wish():
    speak("loading  all driver")
    speak("i am now  online ")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour > 12 and hour < 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")

    speak("I am zera sir how may i help you")
 def joke():
    My_joke = pyjokes.get_joke(language="en", category="neutral")
    speak(My_joke)

def location():
    try:
        ipadd = requests.get('https://api.ipify.org').text
        print(ipadd)
        url = 'https://get.geojs.io/v1/ip/geo/' + ipadd + '.json'
        geo_request = requests.get(url)
        geo_data = geo_request.json()
        city = geo_data['city']
        country = geo_data['country']
        speak(f"i am not sure but I thing we are in{city} city of {country}country ")
    except Exception as e:
        speak("due to network issue I can't find that our  location")

def ip():
    ip = get('https://api.ipify.org').text
    speak(f"your ip address is{ip}")

def wolf():
    # Python program to
    # demonstrate creation of an
    # assistant using wolf ram API



    # Taking input from user
    question = query

    # App id obtained by the above steps
    app_id = "5YAPKH-7XPXAUHT7W"

    # Instance of wolf ram alpha
    # client class
    client = wolframalpha.Client(app_id)

    # Stores the response from
    # wolf ram alpha
    res = client.query(question)

    # Includes only text from the response
    answer = next(res.results).text

    speak(answer)
    print(answer)

def googlenews():
    # BBC news api
    main_url = " http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=35705d33539c42c0a6afe72c405d6613"

    # fetching data in json format
    open_google_page = requests.get(main_url).json()

    # getting all articles in a string article
    article = open_google_page["articles"]

    # empty list which will
    # contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])

    # to read the news out loud for us
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(results)

greetings=["hello","hay","hi"]
greetbot=["hello sir ", "how can I help you", "hola ", "namaste sir", "Well hello sir.", "Welcome and hello sir."]



if __name__ == '__main__':
    wish()
    while True:
        query=takeCommand().lower()
        if query in greetings:
            s=random.choice(greetbot)
            speak(s)
        elif "how are you" in query:
            speak("I am fine as long as you maintain your computer")
        elif "who created you" in query:
            speak(" my develover  created me ")
        elif "open google in browser" in query:
            webbrowser.open(www.google.com)

        elif "on youtube" in query:
            speak("playing  on youtube")
            l = query

            kit.playonyt(l)
        elif "search " in query:
            try:

                # it will perform the Google search
                speak("Searching..." + query)
                speak("\n this is what I found on the web")
                kit.search(query)


            except:

                # Printing Error Message
                speak("I can't find " + query + "plese try again")


        elif "news" in query:
            googlenews()

        elif "location"  in query:
            location()
        elif "ip" in query:
            ip()
        elif "tell me a jokes " in query:
            joke()



        else:
            try:
                wolf()



            except:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                # speak("According to Wikipedia")
                print(results)
                speak(results)







