import smtplib
import ssl
import pyjokes
import webbrowser
import pyttsx3
import datetime
import time
import pywhatkit
import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import *
import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
engine = pyttsx3.init()
bot = ChatBot(name='Andrew', read_only=False,
              logic_adapters=['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.BestMatch'])

trainer = ListTrainer(bot)
trainer.train([
    'hi!',
    'how do you do?',
    'how are you?',
    "I'm cool.",
    'fine, you?',
    'always cool.',
    "I'm ok",
    'glad to hear that.',
    "i'm fine",
    'glad to hear that.',
    'i feel awesome',
    'excellent, glad to hear that.',
    'not so good',
    'sorry to hear that.',])

corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english')
My_joke = pyjokes.get_joke(language="en", category="all")
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)

def send():
    send = "You = "+e.get()
    response = bot.get_response(send)
    txt.insert(END,"\n"+send)
    if e.get() ==[("hi"),('hello')]:
        txt.insert(END, "\n" + "Andrew = Hi,Nice to meet you")
        engine.say('Hi,Nice to meet you')
        engine.runAndWait()
    if e.get() != ".":
        txt.insert(END, "\n" + "Andrew = "+str(response))
        engine.say(response)
        engine.runAndWait()
    if e.get() == "who are you":
        txt.insert(END, "\n" + "Andrew = I'm Andrew,your virtual assistant")
        engine.say("I'm Andrew,your virtual assistant")
        engine.runAndWait()
    if e.get() == "what can you do":
        txt.insert(END, "\n" + "Andrew = I can send emails,open google,youtube,play music,and many more things")
        engine.say('I can send emails,open google,youtube,play music,and many more things')
        engine.runAndWait()
    if e.get() == "open youtube":
        txt.insert(END, "\n" + "Andrew = Opening youtube")
        engine.say('Opening youtube')
        engine.runAndWait()
        webbrowser.open('https://youtube.com')
    if e.get() == "open google":
        txt.insert(END, "\n" + "Andrew = Opening google")
        engine.say('Opening google')
        engine.runAndWait()
        webbrowser.open('https://google.com')
    if e.get() == "open google maps":
        txt.insert(END, "\n" + "Andrew = Opening google maps")
        engine.say('Opening google maps')
        engine.runAndWait()
        webbrowser.open('https://google.com/maps')
    if e.get() == "open google meet":
        txt.insert(END, "\n" + "Andrew = Opening google meet")
        engine.say('Opening google meet')
        engine.runAndWait()
        webbrowser.open('https://meet.google.com')
    if e.get() == "tell me a joke":
        txt.insert(END, "\n" + "Andrew = "+My_joke)
        engine.say(My_joke)
        engine.runAndWait()
    if e.get() == "send an email":
        txt.insert(END, "\n" + "Andrew = Ok,Here we go")
        engine.say('Ok,Here we go')
        engine.runAndWait()
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "aaryanpythondeveloper@gmail.com"
        engine.say('Enter receivers email')
        engine.runAndWait()
        receiver_email = simpledialog.askstring("Input", "Enter receivers email",parent=root)
        engine.say('enter your password')
        engine.runAndWait()
        password = simpledialog.askstring("Input","Type your password and press enter:",parent=root)
        engine.say('Enter your message')
        engine.runAndWait()
        message = simpledialog.askstring("Input","Enter your message :",parent=root)

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            engine.say('email sent')
            engine.runAndWait()
    if e.get() == "news":
        txt.insert(END, "\n" + "Andrew = ")
        engine.say('news')
        engine.runAndWait()
        webbrowser.open('https://news.google.com')
    if e.get() == "send a message":
        person = simpledialog.askstring("Input","To whom should I send :",parent=root)
        if person == 'mom':
            engine.say('To whom should I send')
            engine.runAndWait()
            whatsapp_message = simpledialog.askstring("Input", "What should I send :", parent=root)
            engine.say('What should I send')
            engine.runAndWait()
            pywhatkit.sendwhatmsg('+918806560160',whatsapp_message,2,2)
            engine.say('message sent')
            engine.runAndWait()
    if e.get() == "perform a google search":
        engine.say('Ok,what should I search?')
        engine.runAndWait()
        search = simpledialog.askstring("Input", "Ok,what should I search?:", parent=root)
        pywhatkit.search(search)
    if e.get() == "what is the time":
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        txt.insert(END, "\n" + "Andrew = It is"+ str(current_time))

    if e.get() == "bye":
        engine.say('Bye.See you soon')
        engine.runAndWait()
        txt.insert(END, "\n" + "Andrew = Bye,See you soon.")
        time.sleep(3)
        quit()
    e.delete(0,END)
txt = Text(root)
txt.grid(row=0, column=0,columnspan=5000)
e = Entry(root,width=100)
send = Button(root,text="Send",command=send).grid(row=1,column=1)
e.grid(row=1, column=0)
root.title("Andrew")
root.mainloop()