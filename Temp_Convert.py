# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 22:57:30 2020

@author: pc
*******************
Install Tkinker before running the progrma*****************
"""

from tkinter import *
#convert to Degree Fahrenheight
def convert_fahr():
    words = fbtext.get()
    ftemp = float(words)
    celbox.delete(0, END)
    celbox.insert(0, '%.2f' % (tocel(ftemp)))
    return
#convert to Degree Celcius
def convert_cel():
    words = cbtext.get()
    ctemp = float(words)
    fahrbox.delete(0, END)
    fahrbox.insert(0, '%.2f' % (tofahr(ctemp)))
#Celcious Conversion formular
def tocel(fahr):
    return (fahr-32) * 5.0 / 9.0
#Fahr Conversion Fornular
def tofahr(cel):
    return cel * 9.0 / 5.0 + 32
#************* App GUI************
app = Tk()
app.title('Temp_Converter')

fahrlabel = Label(app, text = 'Fahrenheit (F)')
fahrlabel.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

cellabel = Label(app, text = ' Celsius (C)')
cellabel.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)

fbtext = StringVar()
fbtext.set('')
fahrbox = Entry(app, textvariable=fbtext)
fahrbox.grid(row = 0, column = 1, padx = 5, pady = 5)

cbtext = StringVar()
cbtext.set('')
celbox = Entry(app, textvariable=cbtext)
celbox.grid(row = 1, column = 1, padx = 5, pady = 5)
#*************************buttons*************************
BTNfgo = Button(app, text = '>>>>>>', command = convert_fahr)
BTNfgo.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = N+S+E+W)

BTNcgo = Button(app, text = '<<<<<<<', command = convert_cel)
BTNcgo.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = N+S+E+W)

BTNexit = Button(app, text = 'Exit', command = quit)
BTNexit.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = N+S+E+W, columnspan = 3)

app.mainloop()