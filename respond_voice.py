  
import speech_recognition as sr 
import pyttsx3
import pyjokes

assis_name="Mahi"
boss_name="kumaran Theebath"
def say(text):
    engine=pyttsx3.init()
    voice=engine.getProperty('voices')
    engine.setProperty('voice',voice[0].id)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening.......")
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            print("Recognizing.............")
            text=r.recognize_google(audio,language='en-in')
            print(f"User said : {text}\n")
        except Exception as e :
            print(e)
            print("can not recognize your voice")
            return "None"
        return text

def tell_joke():
    joke=pyjokes.get_joke()
    return joke
    

def respond(text):
    if 'hai' in text:
        say("HI SIR !")
    elif "who are you" in text:
        say("My name is {}".format(assis_name))
    elif "introduce yourself" in text: 
        say("my name is mahi" ) 
        say("im designed by Kumaran Theebath") 
        say("im avirtual assistant ok ma boss")        
    elif "I love you mahi" in text:
        say("i love you to sir")
    elif "who I am" in text: 
        say("If you talk then definately your human.")
    elif 'who are you' in text:
        say("My name is "+assis_name+"!"+"My Boss Name is "+boss_name)
    elif 'where am I' in text:
        say("you are in ")
    elif 'thank you so much' in text:
        say("It's my pleasure Sir!")
    elif 'fine' in text or "good" in text: 
        say("It's good to know that your fine")
    elif 'tell me joke' in text:
        engine2=pyttsx3.init()
        engine2.setProperty('rate',100)
        engine2.say(tell_joke())
        engine2.runAndWait()
    

while True:
    text=takecommand()
    respond(text)