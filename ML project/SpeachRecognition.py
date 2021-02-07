from tkinter import *
from tkinter import ttk
import playsound
import speech_recognition as sr
from gtts import gTTS

def listen_user():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print ('Robttica is listening...')
        audio = rec.listen(source, phrase_time_limit=3)
    try:
        text = rec.recognize_google(audio, language='en-US') 
        return text
    except:
        print("sorry , Iam not leistening") 
        return 0
def talk(text, file):
        tts= gTTS(text= text , lang= "en")
        filename ="%s.mp3"%file
        tts.save(filename)
        playsound.playsound(filename)
def conatct():
    text_returnd = listen_user()
    if text_returnd == "hello":
        talk("hello my friend what is your name","b")
        phrase= listen_user()
        name= phrase.split()[-1]
        talk("your name is %s"%name,"c")
        

root = Tk()
root.title("Robttica")
root.geometry("520x600")
root.resizable(False,False)

rbt = PhotoImage(file = "unnamed.png")
Label(root , image = rbt).place(x=0,y=0)
ttk.Button(root , text = "START", command = lambda:conatct()).grid(column =0 , row = 0 ,padx = 10 ,pady=10, ipadx =1 ,ipady = 10)

root.mainloop()















