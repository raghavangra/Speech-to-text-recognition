# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 23:51:45 2019

@author: Raghav Angra
"""
import tkinter
from tkinter import*
import os
from tkinter.messagebox import showinfo
def newFile():
    pass

def openFile():
    pass

def saveFile():
    pass

def undo():

    textArea.event_generate(("<<Undo>>"))

def redo():
    textArea.event_generate(("<<Redo>>"))

def cut():
    textArea.event_generate(("<<Cut>>"))

def copy():
    textArea.event_generate(("<<Copy>>"))

def paste():
    textArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Code by Raghav Angra")

if __name__=='__main__':
    #setting up tkinter window
    window = tkinter.Tk()
    window.title("Untitled-Notepad")
    window.wm_iconbitmap("a.ico")
    window.geometry("1140x590")

    # create text area
    textArea=Text(window, font= "lucida 13")
    file = None
    textArea.pack(expand=True, fill=BOTH)


    #create menubar
    #File menu
    MenuBar = Menu(window)
    FileMenu = Menu(MenuBar, tearoff=0)
    #to open new file
    FileMenu.add_command(label="New", accelerator="Ctrl+N", command=newFile)
    #to open existing file
    FileMenu.add_command(label="Open", accelerator="Ctrl+O", command=openFile)
    #to save file
    FileMenu.add_command(label="Save", accelerator="Ctrl+S", command=saveFile)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    #Edit menu
    EditMenu = Menu(MenuBar, tearoff=0)
    # undo
    EditMenu.add_command(label="Undo", accelerator="Ctrl+Z", command=undo)
    # redo
    EditMenu.add_command(label="Redo", command=redo)
    # cut
    EditMenu.add_command(label="Cut", accelerator="Ctrl+X", command=cut)
    # copy
    EditMenu.add_command(label="Copy", accelerator="Ctrl+C", command=copy)
    # paste
    EditMenu.add_command(label="Paste", accelerator="Ctrl+V", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    # help menu
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)
    MenuBar.add_cascade(label='Help', menu=HelpMenu)
    window.config(menu=MenuBar)

    # adding scrollbar
    scroll=Scrollbar(textArea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=textArea.yview)
    textArea.config(yscrollcommand=scroll.set)


    window.mainloop()
