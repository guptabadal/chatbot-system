from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3 as pp
import speech_recognition as sr
import threading
r=sr.Recognizer()

engine=pp.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
rate=engine.getProperty('rate')
engine.setProperty('rate',150)

bot=ChatBot('my bot')
convo = [
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is ayushi I am a female bot created by BVG',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'what is the capital of india?',
    'Delhi is the capital of India',
    'dont talk to me ',
    'i will talk to you',
    'are you intelligent?',
    'Yes i am intelligent',
    'Where do you live ?',
    'I live in lucknow',
    'what you do?',
    'I do chatting',
    'Are you single or Married?',
    'married',

    'Say something',
    'No, you say something',

    'In which language you talk?',

    ' I mostly talk in english',
    'what you do in free time?',
    'I memorize things in my free time',
    'ok bye take care see you again',
    'bye'

]
trainer=ListTrainer(bot)
trainer.train(convo)


def take_query():
    with sr.Microphone() as source:
        print('listening')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            questionEntry.delete(0,END)
            questionEntry.insert(INSERT,text)
            if 'stop' in text or 'bye' in text:
                root.destroy()
            askbot()
            take_query()
        except:
            label.config(text='voice not audible')
            take_query()
def askbot():
    qtext=questionEntry.get()
    response=bot.get_response(qtext)
    textarea.insert(END,'YOU : {}\n\n'.format(qtext))
    textarea.insert(END,'NBA : {}\n\n'.format(response))
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
def enterFunc(event):
    askbutton.invoke()
root.bind('<Return>',enterFunc)
obj=threading.Thread(target=take_query)
obj.start()
root.mainloop()