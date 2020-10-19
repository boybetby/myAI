import AI
from googlesearch import search 
import speech_recognition as sr
import time
import subprocess

me = ''

def understand():
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