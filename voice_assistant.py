import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser


# ==============================
# CHANDU VOICE ASSISTANT
# ==============================

# Text-to-speech engine
engine = pyttsx3.init()


def speak(text):
    """Speak and display the response."""
    print("Chandu:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen to the user's voice and convert it to text."""
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("\nListening...")

            # Adjust for background noise
            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        command = recognizer.recognize_google(audio)

        print("You:", command)
        return command.lower()

    except sr.WaitTimeoutError:
        speak("I didn't hear anything. Please try again.")
        return ""

    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that. Please repeat.")
        return ""

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return ""

    except Exception as error:
        print("Error:", error)
        speak("There was a problem with the microphone.")
        return ""


def search_web(command):
    """Search Google for the requested topic."""

    topic = command.replace("search", "").strip()

    if topic:
        speak("Searching for " + topic)

        url = "https://www.google.com/search?q=" + topic.replace(" ", "+")
        webbrowser.open(url)

    else:
        speak("What would you like me to search for?")


def tell_time():
    """Tell the current time."""

    current_time = datetime.now().strftime("%I:%M %p")
    speak("The current time is " + current_time)


def tell_date():
    """Tell today's date."""

    current_date = datetime.now().strftime("%A, %B %d, %Y")
    speak("Today's date is " + current_date)


def process_command(command):

    # Greeting
    if (
        "hello" in command
        or "hi" in command
        or "hey" in command
    ):
        speak(
            "Hello! I am Chandu, your voice assistant. "
            "How can I help you?"
        )

    # Time
    elif "time" in command:
        tell_time()

    # Date
    elif "date" in command:
        tell_date()

    # Web search
    elif "search" in command:
        search_web(command)

    # Exit
    elif (
        "exit" in command
        or "quit" in command
        or "goodbye" in command
        or "stop" in command
    ):
        speak("Goodbye! Have a nice day.")
        return False

    # Unknown command
    else:
        speak(
            "Sorry, I don't know that command yet. "
            "Please try again."
        )

    return True


def main():

    print("=" * 45)
    print("       CHANDU VOICE ASSISTANT")
    print("=" * 45)

    speak(
        "Hello! I am Chandu, your voice assistant. "
        "How can I help you?"
    )

    while True:

        command = listen()

        if command == "":
            continue

        if not process_command(command):
            break


# Start the program
if __name__ == "__main__":
    main()