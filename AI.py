import speech_recognition as sr
import pyttsx3
import subprocess
import time
from googlesearch import search 


AI_hear = sr.Recognizer()
AI_understand = ''
AI_speak = pyttsx3.init()

running = True

while running :
    #hear 
    with sr.Microphone() as mic:
        print("AI: How can i help you?")
        audio = AI_hear.listen(mic)
        print('AI: ...')
    try:        
        me = AI_hear.recognize_google(audio)
        print("Me: "+me)
    except:
        me = ""
        
    #understand
    if me == '':
        AI_understand = 'Im listening'
    elif 'hello' in me.lower():
        AI_understand = 'Hello'   
    elif 'stop' in me.lower():
        running = False    
        AI_understand = 'See you later'
    elif 'steam' in me.lower():
        print('AI: Opening Steam...')
        subprocess.call('F:\Steam\Steam.exe')
        print('Done')
        time.sleep(2)
    elif 'google' or 'search for' or 'find' in me.lower():
        print('Result for: ' +me)
        for i in search(me, tld='com', lang='en', num=10,stop=5, pause=2.0):   
            print(i) 
        me = ''
        
    #speak 
    print('AI: '+AI_understand)      
    AI_speak.say(AI_understand)
    AI_speak.runAndWait()        