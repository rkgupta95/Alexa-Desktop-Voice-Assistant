import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
#import smtplib


engine = pyttsx3.init('sapi5')
sound = engine.getProperty('voices')
#print(sound[0].id)

engine.setProperty('voices', sound[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Alexa sir. Please tell me how may I help you ")

def takeCommand():  #takeCommand funtion return after converting into string,which we say.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

#def sendEmail(to, content):
    #server = smtplib.SMTP('smtp.gmail.com', 587) #Allow less secured apps in gmail
    #server.ehlo()
    #server.starttls()
    #server.login('your-email@gmail.com', 'your-password here')
    #server.sendmail('your-email@gmail.com', to, content)
    #server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        #Logic for executive tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\ravi\\PycharmProjects\\alexa\\song'
            songs = os.listdir(music_dir)
            os.startfile (os.path.join( music_dir , songs[1]))

        elif 'the time' in query:
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open studio' in query:
            studioPath = "C:\\Program Files (x86)\\Microsoft Visual Studio 11.0\\Common7\\IDE\\devenv.exe"
            os.startfile(studioPath)

        #elif 'email to ravi' in query:
            #try:
                #speak("what should I say?")
                #content = takeCommand()
                #to = "ravi-your-email@gmail.com"
                #sendEmail(to, content)
                #speak("Email has been sent!")
            #except Exception as e:
                #print(e)
                #speak("Sorry ravi.I am not able to send this email")
