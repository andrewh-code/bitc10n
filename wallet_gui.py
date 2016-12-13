#!/usr/bin/python 

# include libraries
import os
import sys
import pyelliptic
from tkinter import * # lowercase t for python 3.x


class WalletApplication(Frame):
    # Wallet 
    # have one input field 
    # have two buttons, two text/label fields
    # input field - for the name of the user owning the specific Wallet
    # one button to generate the public/private key-pair
    # the other button saves the private/public key to the keystore (file)
    # the two text/label fields show the public/private keys

    # class variables
    
    # constructor method
    def __init__(self, master):     # pass in width and height
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # create buttons
        self.button1 = Button(self, text = "button1")
        self.button1.grid(row = 0, column = 0)

        # second button
        self.button2 = Button(self, text = "button2")
        self.button2.grid(row = 4, column = 0)


if __name__ == '__main__':
    # declare constants
    TITLE = "Bitc10n wallet"
    SIZE = "400x400"

    # instantiate tk object
    root = Tk()
    root.title(TITLE)
    root.geometry(SIZE)
    app = WalletApplication(root)
    
    # run wallet
    root.mainloop()
