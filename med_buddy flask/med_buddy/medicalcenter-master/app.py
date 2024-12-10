from flask import Flask, render_template, request, jsonify
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import openai
import sched
import time

app = Flask(__name__) 

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Schedule for reminders
scheduler = sched.scheduler(time.time, time.sleep)

# Function to speak audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to get the current time
def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is " + current_time)
    print("The current time is ", current_time)

# Function to get the current date
def get_date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    date_str = f"{day}/{month}/{year}"
    speak("The current date is " + date_str)
    print(date_str)

# Function to remind to take tablets
def remind_to_take_tablet():
    hour = datetime.datetime.now().hour
    if hour == 9 and datetime.datetime.now().minute == 30:
        speak("Good morning buddy, it's time to take your morning tablet.")
    elif hour == 14 and datetime.datetime.now().minute == 0:
        speak("Good afternoon buddy, it's time to take your afternoon tablet.")
    elif hour == 20 and datetime.datetime.now().minute == 30:
        speak("Good evening buddy, it's time to take your evening tablet.")
    scheduler.enter(60, 1, remind_to_take_tablet)

def wishme():
    print("Welcome back buddy!!")
    speak("Welcome back buddy!!")
    
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning !!")
        print("Good Morning !!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon !!")
        print("Good Afternoon !!")
    elif hour >= 16 and hour < 24:
        speak("Good Evening !!")
        print("Good Evening !!")
    else:
        speak("Good Night Sir, see you tomorrow")

    speak("Medbuddy at your service buddy, please tell me how may I help you.")
    print("Medbuddy at your service buddy, please tell me how may I help you.")

# Function to take screenshot
def screenshot():
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("~\\Pictures\\ss.png")
    img.save(img_path)
    return img_path

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        print("Listening...")

        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query

# Function to get OpenAI response
def get_openai_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
            )
        return response.choices[0].text.strip()
    except Exception as e:
        return "Sorry, I couldn't process the request."

# Flask route for index
@app.route('/')
def index():
    return render_template('index.html')

# Flask route to process commands
@app.route('/ai', methods=['POST'])
def start():
    wishme()
    while True:
        data = request.json  
        query = data.get('query', '').lower() 
        if "time" in query:
            get_time()

        elif "date" in query:
            get_date()

        elif "who are you" in query:
            speak("I'm Medbuddy created by team crewX and I'm a desktop voice assistant.")
            print("I'm Medbuddy created by team crewX and I'm a desktop voice assistant.")

        elif "how are you" in query:
            speak("I'm fine sir, what about you?")
            print("I'm fine sir, what about you?")

        elif "fine" in query or "good" in query:
            speak("Glad to hear that buddy!!")
            print("Glad to hear that buddy!!")

        elif "wikipedia" in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page buddy, please ask something else")

        elif "open youtube" in query:
            wb.open("youtube.com")

        elif "open google" in query:
            wb.open("google.com")

        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        elif "play music" in query:
            song_dir = os.path.expanduser("~\\Music")
            songs = os.listdir(song_dir)
            print(songs)
            x = len(songs)
            y = random.randint(0, x - 1)
            os.startfile(os.path.join(song_dir, songs[y]))

        elif "open chrome" in query:
            speak("What should I search?")
            search = takecommand().lower()
            wb.open(f"https://www.google.com/search?q={search}")
            print(f"Searching for {search} on Chrome")

        elif "remember that" in query:
            speak("What should I remember?")
            data = takecommand()
            speak("You said me to remember that " + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that " + remember.read())
            print("You told me to remember that " + str(remember))

        elif "screenshot" in query:
            screenshot()
            speak("I've taken a screenshot, please check it")

        elif "offline" in query:
            quit()
        
        elif "search on chrome" in query:
            try:
                speak("What should I search?")
                print("What should I search?")
                chromePath = "www.ch"
                search = takecommand()
                wb.get(chromePath).open_new_tab(search)
                print(search)
                speak("What should I search?")
                print("What should I search?")
                url = takecommand()
                wb.open_new_tab(url)
                print("Opening:", url)
            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")
        return jsonify({"message": "Query processed successfully"})


if __name__ == "__main__":
    app.run(debug=True)
