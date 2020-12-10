# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 23:57:30 2020

@author: pc

""
The computer guesses a number and the user provides the hints.
*******************INSTALLATION**************
Download breezypythongui using the link:::
http://kennethalambert.com/breezypythongui/downloads.html

After downloading breezypythongui, you unzip the file and place the file breezypythongui.py in a place where your Python can get to it.
This can be the current working directory where you launch Python,the directory where your GUI applications will be located,
 or Python's system directory where third-party libraries are kept.
"""
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

        self.myLabel = self.addLabel(text=guess, row=0, column=0, sticky="NSEW", columnspan=4)

        self.small = self.addButton(text="Too small", row=1, column=0, command=self.goLarge)

        self.large = self.addButton(text="Too large", row=1, column=1, command=self.goSmall)

        self.correct = self.addButton(text="Correct", row=1, column=2, command=self.goCorrect)

        self.newButton = self.addButton(text="New game", row=1, column=3, command=self.newGame)

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
        self.myLabel['text'] = f" Yeah! You guessed it Correct  in {self.count} tries. Press New Game to start a new game!"
        self.small["state"] = "disabled"
        self.large["state"] = "disabled"
        self.correct["state"] = "disabled"

    def newGame(self):
        self.upperBound = 100
        self.lowerBound = 1
        self.count = 0
        self.update()
        self.small["state"] = "active"
        self.large["state"] = "active"
        self.correct["state"] = "active"

#main function that calls the class
def main():
    game1 = GuessingGame()
    game1.mainloop()

if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\nProgram closed.")
