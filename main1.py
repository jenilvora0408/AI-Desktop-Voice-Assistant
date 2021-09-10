import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

# For the use of inbuilt window voice
engine = pyttsx3.init('sapi5')

# Fetches inbuilt window voices
voices = engine.getProperty('voices')
# print(voices[0].id)

# If multiple voices are available, we can set it by writing this;
engine.setProperty('voice', voices[0].id)


def speak(audio):
    '''
    engine (zira) will speak audio string
    '''
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    '''
    It will wish me with respect to time
    '''
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Zira sir, Please tell me how may i help you?")


def takeCommand():
    '''
    It takes microphone input from the user and returns string output
    '''
    # It will help us recognize the audio
    r = sr.Recognizer()

    # I want to use microphone as source
    with sr.Microphone() as source:
        print("Listening...")
        # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
        r.pause_threshold = 1

        # Uncomment the below line if there is a background noise & you want to ignore it.
        #r.energy_threshold = 350
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Don't forget to mention your mail-id & password in below code
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

    # Logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace('wikipedia', '')
        results = wikipedia.summary(query, sentences=2)
        speak('According to wikipedia')
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'play music' in query:

        # Don't forget to change file path if you import my program
        music_dir = 'E:\\Songs'

        # Lists all the files present inside the directory
        songs = os.listdir(music_dir)
        print(songs)

        # We can use random module in order to generate a no. and play different music
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, The time is {strTime}")

    elif 'send email' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            # Write the mail-id to whom you want to send Email
            to = "iAmAnIndian@gmailcom"
            sendEmail(to, content)
            speak("Email has been sent")

        except Exception as e:
            print(e)
            speak("Sorry sir, unable to send mail.")
