# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 02:48:27 2019

@author: Raghav Angra
"""

import tkinter
from tkinter import*
import os
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import speech_recognition as sr
import sys


def listen():
    #Recognizer function to recognize the speech
    r=sr.Recognizer()
    #capture the speech
    with sr.Microphone() as source:
        audio=r.listen(source, timeout=None, phrase_time_limit=None) #speech stored in audio variable
    #Passing audio to google API to predict the text
    try:
        textDisplay.insert(tkinter.END, r.recognize_google(audio))
    except Exception:
        textDisplay.insert("Something went wrong!")



def openFile():
    global file
    #choose a .wav file to be recognized
    file = askopenfilename(defaultextension=".wav", filetypes=[("All Files", "*.*")])

    #Recognizer function to recognize the speech
    r=sr.Recognizer()
    #capture the choosen file
    with sr.AudioFile(file) as source:
        audio=r.listen(source, timeout=None, phrase_time_limit=None) #speech stored in audio variable
    #Passing audio to google API to predict the text
    try:
        textDisplay.insert(tkinter.END, r.recognize_google(audio))
    except Exception:
        textDisplay.insert("Something went wrong!")



def Quit():
    window.destroy()



def clear():
    textDisplay.delete("1.0", tkinter.END)



def save():
    global file
    file = asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*")])
    # asksaveasfile returns None if dialog closed with "cancel".
    if file is None:
        return
    textSave=str(textDisplay.get(1.0, tkinter.END))
    #open blank file in write mode
    f= open(file, "w")
    f.write(textSave)
    f.close()




if __name__=='__main__':
    #setting up tkinter window
    window = tkinter.Tk()
    window.configure(background="black")
    window.title("Speech to Text Converter")
    window.wm_iconbitmap("text.ico")
    window.geometry("840x490")

    #Label display
    label=tkinter.Label(window, text="Speech to Text Converter")
    label.config(font=("Times New Roman",44))
    label.pack(fill=tkinter.X, padx=30, pady=10, ipady=10 )

    #Speak button
    button1=tkinter.Button(window, fg="black", width=13, text="Speak", font=("Times New Roman",20), command=listen)
    button1.place(x=30, y=155)

    #chooseFile button
    button2=tkinter.Button(window, fg="black", width=13, text="Choose File", font=("Times New Roman",20), command=openFile)
    button2.place(x=30, y=215)

    #Save text button
    saveText=tkinter.Button(window, fg="black", width=13, text="Save Text", font=("Times New Roman",20), command=save)
    saveText.place(x=30, y=275)

    #clear text button
    clearText=tkinter.Button(window, fg="black", width=13, text="Clear", font=("Times New Roman",20), command=clear)
    clearText.place(x=30, y=335)

    #quit button
    quitButton=tkinter.Button(window, fg="black", width=13, text="Quit", font=("Times New Roman",20), command=Quit)
    quitButton.place(x=30, y=395)

    #display area
    textDisplay=tkinter.Text(window, height=13, width=48)
    textDisplay.place(x=276, y=150)
    textDisplay.config(font=("Times New Roman",16))


    window.mainloop()
