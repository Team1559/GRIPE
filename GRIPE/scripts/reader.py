#!/usr/bin/python

import sys
import numpy as np

target = open('config.gripe', "r")

target.seek(0)
data = target.read()

stringlist = data.split("\n")

hhigh = stringlist[0]
shigh = stringlist[1]
vhigh = stringlist[2]
hlow = stringlist[3]
slow = stringlist[4]
vlow = stringlist[5]
brightness = stringlist[6]

lowValues = np.array((hlow,slow,vlow))
highValues = np.array((hhigh,shigh,vhigh))

print lowValues
print highValues
print brightness
