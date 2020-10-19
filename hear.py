import speech_recognition as sr

AI_hear = sr.Recognizer()
with sr.Microphone() as mic:
    print("How can i help you?")
    audio = AI_hear.listen(mic)

try:        
    me = AI_hear.recognize_google(audio)
except:
    me == ""
    
print(me)    
    