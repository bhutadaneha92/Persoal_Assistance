import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def wishme(datetime):
  hour = int(datetime.datetime.now().hour)
  if hour >= 0 and hour < 12:
    speak("good morning Neha")
  elif hour > 12 and hour < 18:
    speak("good afternoon Neha")
  else:
    speak("good evining Neha")

speak("Hey Neha, jarvis here please let me know how can i help you?")

def takecommand():
  #It take a microphone input from user and returns string output
  r = sr.Recognizer()
  
  with sr.Microphone() as source:
    print("listening....")
    r.pause_threshold = 1
    audio = r.listen(source)
  
  try:
    print("recognizing...")
    query = r.recognize_google(audio, language = "en-in")
    print("user said:",query)
  except Exception as e:
    print(e)
    speak("say that again please....")
    return "none"
  return query

if __name__ == '__main__':
  #speak()
  wishme(datetime)

  if 1:
    query = takecommand().lower()

    if 'wikipedia' in query:
      speak("searching wikipedia....please wait for a while")
      query = query.replace("wikipedia","")
      results = wikipedia.summary(query,sentences = 2)
      speak("According to wikipedia")
      print(results)
      
    elif 'open youtube' in query:
      webbrowser.open("youtube.com")

    elif 'open google' in query:
      webbrowser.open("google.com")

    elif 'open notepad' in query:
      npath = 'C:\\Windows\\system32\\notepad.exe'
      os.startfile(npath)

    elif 'open command prompt' in query:
      os.system('start cmd')

    elif 'open stackoverflow' in query:
      webbrowser.open('stackoverflow.com')

    elif 'open calender' in query:
      webbrowser.open('calender.com')

    elif 'open code' in query:
      codepath = "D:\\AI class\\ML\\ML\\Personal Assistant\\Personal_Assistant.py"
      os.startfile(codepath)

    elif 'time' in query:
      strtime = datetime.datetime.now().strftime("%m/%d/%Y, %I:%M %p")
    #%H:%M:%S"
      speak(f"The time is {strtime}")
      print(strtime)

    elif 'no thanks' in query:
      speak("Thank you for using me Have a good day")

sys.exit()
    
