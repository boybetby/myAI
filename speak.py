import pyttsx3

def speak():
    AI_understand = ''
    AI_speak = pyttsx3.init()
    AI_speak.say(AI_understand)
    AI_speak.runAndWait()