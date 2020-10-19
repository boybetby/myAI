import speech_recognition as sr

def hear(n): 
    with sr.Microphone() as mic:
        print("AI: How can i help you?")
        audio = AI_hear.listen(mic)
        print('AI: ...')
        try:        
            me = AI_hear.recognize_google(audio)
            print("Me: "+me)
        except:
            me = ""
        
        #knowledge    
        if me is not None:
            n+=1
            for i in range (0,n) :
                a.append(me)