# Python-GUI-Projects

Project #3: 
#Temperature Conversion GUI

#convert to Degree Fahrenheight
def convert_fahr():
 words = fbtext.get()
 ftemp = float(words)
 celbox.delete(0, END)
 celbox.insert(0, '%.2f' % (tocel(ftemp)))
 return
 *************************************************
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


Project #5: Guess the Number Game GUI
The computer guesses a number and the user provides the hints.

import random
from breezypythongui import EasyFrame
#Guess Game main Class
class GuessingGame(EasyFrame):
#class defination
 def __init__(self):
 EasyFrame.__init__(self, title="Number Guessing Game")
 self.lowerBound = 1
 self.upperBound = 100
 self.count = 0
 self.myNumber = (self.lowerBound + self.upperBound) // 2
 guess = "Is my Guess of " + str(self.myNumber) + " Right?"
 self.myLabel = self.addLabel(text=guess, row=0, column=0, sticky="NSEW",
columnspan=4)
 self.small = self.addButton(text="Too small", row=1, column=0,
command=self.goLarge)
 self.large = self.addButton(text="Too large", row=1, column=1,
command=self.goSmall)
 self.correct = self.addButton(text="Correct", row=1, column=2,
command=self.goCorrect)
 self.newButton = self.addButton(text="New game", row=1, column=3,
command=self.newGame)
# Updates the Computer Guess if the attempt is not correct
 def update(self):
 self.myNumber = (self.lowerBound + self.upperBound) // 2
 guess = "Is my Guess of " + str(self.myNumber) + " Right?"
 self.myLabel['text'] = guess
 # check if the guess is larger than the exact number
 def goLarge(self):
 self.lowerBound = self.myNumber + 1
 self.count += 1
 self.update()
#check if the guess is smaller than the exact number
 def goSmall(self):
 self.upperBound = self.myNumber - 1
 self.count += 1
 self.update()
#check if the guess is correct
 def goCorrect(self):
 self.count += 1
 self.myLabel['text'] = f" Yeah! You guessed it Correct in {self.count}
tries. Press New Game to start a new game!"
 self.small["state"] = "dis
