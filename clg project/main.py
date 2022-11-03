from datetime import datetime
import  webbrowser
import pyttsx3
import speech_recognition as sr
from time import sleep
import time
import wikipedia
import os
from os import startfile
import pyautogui
from keyboard import press
from keyboard import write
from email import message
import subprocess
from notepad import opennotepad, takeCommand2





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

def ChromeAuto(command):
          

          query = str(command)

          if 'new tab' in query:

               press_and_release('ctrl + t')

          elif 'close tab' in query:

                  press_and_release('ctrl + w')

          elif 'new window' in query:

                   press_and_release('ctrl + n')

          elif 'history' in query:

                press_and_release('ctrl + h')

          elif 'download' in query:

                 press_and_release('ctrl + j')

          elif 'bookmark' in query:

                 press_and_release('ctrl + d')

                 press('enter')

          elif 'incognito' in query:

                  press_and_release('Ctrl + Shift + n')

          elif 'switch tab' in query:

                 tab = query.replace("switch tab ", "")
                 Tab = tab.replace("to","")
        
                 num = Tab

                 bb = f'ctrl + {num}'

                 press_and_release(bb)

          elif 'open' in query:

               name = query.replace("open ","")

               NameA = str(name)

          if 'youtube' in NameA:

            web.open("https://www.youtube.com/")

          elif 'instagram' in NameA:

                web.open("https://www.instagram.com/")

          else:

            string = "https://www." + NameA + ".com"

            string_2 = string.replace(" ","")

            web.open(string_2)

        
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
          elif'whatsapp' in query:
               speak("openin whatsapp please waitt")
              
               var="C:\\Users\\Admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
               os.startfile(var)
               sleep(10)
          elif'chrome' in query:
               speak("opening chrome")
               p="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
               os.startfile(p)
               query=query.replace("chrome","")
          elif'notepad' in query:
              
               opennotepad()
               takeCommand2()
               
                      
               
               
               
           
         
              
              
                    
              
              



