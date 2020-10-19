import speech_recognition as sr
import pyttsx3
import subprocess
import time
from googlesearch import search 
import understand
import hear
import speak

AI_hear = sr.Recognizer()
AI_understand = ''
AI_speak = pyttsx3.init()

running = True

a = []
n = 0

while running :
    hear(n);
    understand()
    speak()        