import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use female voice

def talk(text):
    print("🎙️ COCO:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("🗣️ You said:", command)
    except sr.UnknownValueError:
        talk("Sorry bro, I didn’t catch that.")
        return ""
    except sr.RequestError:
        talk("Network issue with Google service.")
        return ""
    return command

def run_coco():
    command = take_command()

    if "play" in command:
        song = command.replace("play", "").strip()
        talk(f"Playing {song} on YouTube 🎶")
        pywhatkit.playonyt(song)

    elif "what's the time" in command or "what is the time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"It’s {time} ⏰")

    elif "who is sambhav" in command or "who is sambhav_codes" in command:
        info = (
            "Sambhav, known for creative coding content, is a Python project developer. "
            "He shares cool projects and tutorials 💻"
        )
        talk(info)

    elif (
        "who is" in command
        or "what is" in command
        or "search wikipedia for" in command
        or "tell me about" in command
    ):
        topic = command
        for phrase in ["who is", "what is", "search wikipedia for", "tell me about"]:
            topic = topic.replace(phrase, "")
        topic = topic.strip()
        try:
            talk(f"Let me look up {topic} on Wikipedia 📚")
            info = wikipedia.summary(topic, sentences=2)
            talk(info)
        except wikipedia.exceptions.DisambiguationError:
            talk(f"There are many results for {topic}. Try being more specific.")
        except wikipedia.exceptions.PageError:
            talk(f"Sorry, I couldn’t find any page about {topic}.")
        except:
            talk("Something went wrong while fetching data from Wikipedia.")

    elif "search google for" in command or "google" in command:
        search_query = command.replace("search google for", "").replace("google", "").strip()
        talk(f"Searching Google for {search_query} 🔍")
        pywhatkit.search(search_query)

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "open chrome" in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            talk("Opening Chrome 🚀")
            os.startfile(chrome_path)
        else:
            talk("Chrome path not found.")

    elif "open code" in command or "open vs code" in command:
        talk("Opening VS Code 💻")
        os.system("code")

    elif "exit" in command or "stop" in command:
        talk("Okay bro, see you later 👋")
        sys.exit()

    elif command != "":
        talk("I heard you, but I don’t understand that yet.")

# Start the assistant
talk("Yo! I'm COCO – your personal voice assistant 🎤")
while True:
    run_coco()
