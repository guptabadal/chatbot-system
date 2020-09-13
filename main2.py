from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3 as pp
import speech_recognition as sr
import threading
import os
import time
r=sr.Recognizer()

engine=pp.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
rate=engine.getProperty('rate')
engine.setProperty('rate',150)

bot=ChatBot('my bot')
trainer=ListTrainer(bot)
for files in os.listdir(r'/chatBot/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    data=open(r'/chatBot/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
    trainer.train(data)


def take_query():
    with sr.Microphone() as source:
        print('listening')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            questionEntry.delete(0,END)
            questionEntry.insert(INSERT,text)
            if 'stop' in text or 'bye' in text:
                askbot()
                time.sleep(2)
                root.destroy()
            askbot()
        except:
            label.config(text='voice not audible')
def askbot():
    label.config(text='')
    qtext=questionEntry.get()
    response=bot.get_response(qtext)
    textarea.insert(END,'YOU : {}\n\n'.format(qtext))
    textarea.insert(END,'bad BOT : {}\n\n'.format(response))
    questionEntry.delete(0,END)
    engine.say(response)
    textarea.yview(END)
    engine.runAndWait()






###########GUI####################
root=Tk()
root.geometry('500x600+100+30')
root.resizable(0,0)
root.title('Chatbot by BVG')
root.config(bg='dimgray')
pic=PhotoImage(file='pic.png')
picture_label=Label(root,image=pic,bg='dimgray')
picture_label.pack(pady=10)
centerframe=Frame(root)
centerframe.pack(pady=10)
scrollbar=Scrollbar(centerframe)
scrollbar.pack(side='right',fill=Y)
textarea=Text(centerframe,font=('arial',18,'bold'),width=80,height=10,yscrollcommand=scrollbar.set)
textarea.pack(side='left',fill=BOTH)
lowerframe=Frame(root,bg='dimgray')
lowerframe.pack()
questionEntry=Entry(lowerframe,font=('verdana',25,'bold'))
questionEntry.pack(fill='x',pady=5)
label=Label(lowerframe,text='',bg='dimgray')
label.pack(pady=1)
askimage=PhotoImage(file='ask.png')
askbutton=Button(lowerframe,image=askimage,bd=0,bg='dimgray',activebackground='dimgray',cursor='hand2',command=askbot)
askbutton.pack(pady=0)
def repeat():
    while True:
        take_query()
def enterFunc(event):
    askbutton.invoke()
root.bind('<Return>',enterFunc)
obj=threading.Thread(target=repeat)
obj.setDaemon(True)
obj.start()
root.mainloop()