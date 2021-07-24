import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")   

    else:
        speak("Good Evening sir")  

    speak("hai  iam mahi. im a virtual assistant of kumaran theebath verson 2.0") 
    speak("Please tell me how may I help you") 


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
  
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/kumaran_theebath/")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/kumaran.theebath/")
        elif'play music' in query:
             musicdlr="D:\\SONGS"
             songs=os.listdir(musicdlr)
             print(songs)
             os.startfile(os.path.join(musicdlr,songs[1]))
        

        elif'open viber' in query:
             os.startfile('C:\\Users\\Venus\\AppData\\Local\\Viber\\Viber.exe')
        elif'open zoom' in query:
             os.startfile('C:\\Users\\Venus\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
        elif'open word' in query:
            os.startfile('"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"')
        elif'open chrome'in query:
            os.startfile('C:\\Users\\Venus\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe')
        
        elif 'close' in query:
            query=query.replace("close"," ") 
            if 'viber' or 'Viber'  in query:
             os.system("TASKKILL /F /IM viber.exe")
            if 'zoom' or 'Zoom' in query:
             os.system("TASKKILL /F /IM zoom.exe")
            if 'word' or 'Word' in query:
             os.system("TASKKILL /F /IM word.exe")  
            if 'chrome' or 'Chrome' in query:
             os.system("TASKKILL /F /IM chrome.exe") 
        elif 'the time'  in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        
        
            


            
              

        


    

        

        

        