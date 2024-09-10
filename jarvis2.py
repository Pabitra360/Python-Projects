import speech_recognition as sr
import os
import webbrowser
import datetime


def speak(text):
    """Use macOS's 'say' command to speak the text."""
    os.system(f"say {text}")


def listen_to_command():
    """Listen for a voice command and return the recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold =0.6
        print("Listening...")
        audio_data = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio_data, language="en-in")
            print(f"User said: {command}")
            return command
        except sr.UnknownValueError:
            return "Sorry, I did not understand the audio."
        except sr.RequestError:
            return "Could not request results; check your network connection."
        except Exception as e:
            return f"An error occurred: {str(e)}"


def open_website(command):
    """Open a website based on the command received."""
    websites = {
        "youtube": "https://www.youtube.com",
        "wikipedia": "https://www.wikipedia.com",
        "google": "https://www.google.com"
    }

    command = command.lower()
    for site, url in websites.items():
        if f"open {site}" in command:
            speak(f"Opening {site}...")
            webbrowser.open(url)
            return
    speak("Website not recognized or not set up yet.")


def tell_time():
    """Speak the current time."""
    now = datetime.datetime.now()
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    speak(f"Sir, the time is {hour} hours and {minute} minutes.")


def open_application(application_path):
    """Open a specified application."""
    os.system(f"open {application_path}")


if __name__ == '__main__':
    speak("Hello boss, I am Friday A.I")

    while True:
        command = listen_to_command()

        if command:
            if "open music" in command.lower():
                music_path = "/Users/pabitradas/Downloads/Kun Faaya Kun - Rockstar.mp3"
                os.system(f"open {music_path}")

            elif "the time" in command.lower():
                tell_time()

            elif "open facetime" in command.lower():
                open_application("/System/Applications/FaceTime.app")

            elif "open safari" in command.lower():
                open_application("/System/Volumes/Preboot/Cryptexes/App/System/Applications/Safari.app")

            elif "open chat gpt" in command.lower():
                open_application("/Applications/ChatGPT.app")

            # Add more commands as needed