#!/usr/bin/python

###Graphical program to test HSV and brightness values with OpenCV###
###Author Will Merges###
###Team 1559 Deviltech###


from Tkinter import *
import numpy as np
import sys
import cv2
import camerafeed


###USE SLIDERS WITH "Scale" function instead of entries later###


class Gui(object):

    def __init__(self):

        #setup window
        global window
        window = Tk()
        window.title("GRIPE")
        #window.geometry("640x480")
        window.configure(background='grey')

        #add stuffs
        self.addIcon()
        self.addLabels()
        self.addEntries()
        self.addButts()

        #create the camera feed
        global c
        c = camerafeed.CameraFeed()

        #update once for the camera feed
        self.update()


    def addLabels(self):

        #Labels
        Label(window, text="H Low Value").grid(row=0)
        Label(window, text="H High Value").grid(row=1)
        Label(window, text="S Low Value").grid(row=2)
        Label(window, text="S High Value").grid(row=3)
        Label(window, text="V Low Value").grid(row=4)
        Label(window, text="V High Value").grid(row=5)
        Label(window, text="Brightness").grid(row=6)
        #Label(window, text="Write Path").grid(row=9)


    def addEntries(self):

        #Entries
        global e1,e2,e3,e4,e5,e6,e7,e8
        e1 = Entry(window)
        e2 = Entry(window)
        e3 = Entry(window)
        e4 = Entry(window)
        e5 = Entry(window)
        e6 = Entry(window)
        e7 = Entry(window)
        e8 = Entry(window)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        e4.grid(row=3, column=1)
        e5.grid(row=4, column=1)
        e6.grid(row=5, column=1)
        e7.grid(row=6, column=1)
        e8.grid(row=9, column=1)

        #standard values
        e1.insert(10, "0")
        e2.insert(10, "180")
        e3.insert(10, "0")
        e4.insert(10, "255")
        e5.insert(10, "0")
        e6.insert(10, "255")
        e7.insert(10, "0")
        e8.insert(10, "Your File Path Here") #change to project folder later


    def addButts(self):

        #Buttons
        Button(window, text="Update", command=lambda : self.update()).grid(row=7, column=0, sticky=W, pady=4)
        #Button(window, text="Write", command=lambda : c.writeImage()).grid(row=7, column=1, sticky=W, pady=4)
        Button(window, text="Write File", command=lambda : self.write()).grid(row=7, column=1, sticky=W, pady=4)


    def addIcon(self):

        path = 'lib/gripe.ico'
        window.iconbitmap(path)


    def update(self):

        global hlow, hhigh, slow, shigh, vlow, vhigh, brightness, path
        hlow = int(e1.get())
        hhigh = int(e2.get())
        slow = int(e3.get())
        shigh = int(e4.get())
        vlow = int(e5.get())
        vhigh = int(e6.get())
        brightness = int(e7.get())

        c.putLowerRange(hlow,slow,vlow)
        c.putUpperRange(hhigh,shigh,vhigh)
        c.putBrightness(brightness)

        #print hlow,hhigh,slow,shigh,vlow,vhigh,brightness


    def write(self):

        #set the write path
        self.path = e8.get()
        c.setPath(self.path)

        #write the file
        c.writeFile()


    #def getLowerRange():
        #return np.array((hlow,slow,vlow))

    #def getUpperRange():
        #return np.array((hhigh,shigh,vhigh))

    #def getBrightness():
        #return brightness


if __name__ == '__main__':
    g = Gui()
    mainloop()
