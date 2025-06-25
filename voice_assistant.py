import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

def run_assistant():
    speak("Hello, I am your assistant. How can I help you?")
    while True:
        command = get_command()
        if "hello" in command:
            speak("Hello! How are you today?")
        elif "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {now}")
        elif "date" in command:
            today = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")
        elif "search" in command:
            query = command.replace("search", "")
            speak(f"Searching the web for {query}")
            pywhatkit.search(query)
        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break
        elif command:
            speak("Sorry, I can't do that yet. Try asking something else.")

run_assistant()
