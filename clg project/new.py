from datetime import datetime
import  webbrowser
import pyttsx3
import speech_recognition as sr
import  time
import wikipedia
import os
import pyautogui


engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voices', voices[0].id)

def speak(audio):
     """ this function is speak function who will return  voices """
     engine.say(audio) 
     engine.runAndWait()

def takecommand():
     """it will take input in the audio format by using  microphones"""
     r=sr.Recognizer()
     with sr.Microphone() as source:
          print("listeniing........")
          r.pause_thershold =1
          """this thershold function will wait for 2 sec if we speak slowly beacuse we set the pause threshold function at 2 """
          audio =r.listen(source)
     try:
          print("reconging....")
          query = r.recognize_google(audio, language='eng-in')
          print( f"User said: {query}\n")
         
     except Exception as e:
          print(e)
         
          print("say that again please")
          return "None"
     return query       



     


def wishme():
     """ this function will wish us according to time"""
     hour  = int(datetime.now().hour)
     if hour>=0  and hour<12:
          speak("hiii good morning")
     elif hour>=12 and hour<18:
          speak("hiii  good afternoonn")
     else:
          speak("hii good evening")
     speak(" i am jarvis how can i help you")
     
if __name__=="__main__" :

      wishme()


      """ now we have done aur total prepartion and now we will design aur logic for difeerent tasks that our program can execute """
      while True:
          query=takecommand() .lower()

          if'wikipedia' in query:

               """this part will open wikipedia for us and search our  in the program """
               speak('searching wikipedia please wait')
               query= query.replace("wikipedia", "")
               results = wikipedia.summary(query,sentences=2)
               speak("according to our web research")
               speak(results)
               
          elif'youtube' in query:
               speak("searching youtube please wait")
               query=query.replace("youtube","")
               
               webbrowser.open("youtube.com")
          elif 'open google' in query:
                webbrowser.open("google.com")
          
         
              
              
                    
              
              



