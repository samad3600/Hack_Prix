import pywhatkit
import pyttsx3
import speech_recognition as sr
from datetime import timedelta, datetime

# Initialize text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio: str) -> None:
    """Convert text to speech."""
    engine.say(audio)
    engine.runAndWait()


def takeCommand() -> str:
    """Listen to the user's voice command and convert it to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again please.")
        return "None"
    return query.lower()


# Current time and message scheduling time
strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now() + timedelta(minutes=2)).strftime("%M"))

# Mapping persons to their phone numbers
contacts = {
    "samad": "+917287898011",
    "cheese cake": "+919100437353",
    "taha": "+919701825002",
    "razzaq": "+919154319097",
    "mazz": "+919676602978",
    "ayman": "+917995075757"
}


def send_whatsapp_message(phone_number: str, message: str) -> None:
    """Send a WhatsApp message using pywhatkit."""
    pywhatkit.sendwhatmsg(phone_number, message, time_hour=strTime, time_min=update)


def sendMessage() -> None:
    """Get the recipient and message details from the user and send a WhatsApp message."""
    speak("Who do you want to message?")
    print("Person options: Samad, Farad, Taha, Razzaq, Mazz, Ayman")

    person = takeCommand()
    if person in contacts:
        speak("What's the message?")
        message = takeCommand()
        send_whatsapp_message(contacts[person], message)
    else:
        speak("Invalid person name.")

