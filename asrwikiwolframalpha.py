# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 07:43:24 2019

@author: MISBAH KHAN
"""

import wikipedia
import wolframalpha
import speech_recognition as sr
import pyttsx3 
import time 


r = sr.Recognizer()
engine = pyttsx3.init()  
while True:
    with sr.Microphone() as source:
        print('speak..')
        audio= r.listen(source)
        print('Done')
#    my_input = input("Question: ")
        try:
            my_input=r.recognize_google(audio)
        except sr.UnknownValueError:
            print ('Error')
        except sr.RequestError as e:
            print(e)
    
        try:
       
            app_id = "352LJT-6XX2VEVEA7"
            client = wolframalpha.Client(app_id)
            res = client.query(my_input)
            answer = next(res.results).text 
            print(answer)
            engine.say(answer) 
            engine.runAndWait() 

        except:
    
            #print(wikipedia.summary(my_input,sentences=2))
            try:
                wikiresult=wikipedia.summary(my_input,sentences=1)
            except sr.UnknownValueError:
                print ('Error')
            except sr.RequestError as e:
                print(e)
            print(wikiresult)
            engine.say(wikiresult) 
            engine.runAndWait() 
            time.sleep(5)
            
            