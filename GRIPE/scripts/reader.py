#!/usr/bin/python

import sys
import numpy as np

target = open('config.gripe', "r")

target.seek(0)
data = target.read()

stringlist = data.split("\n")

hlow = stringlist[0]
slow = stringlist[1]
vlow = stringlist[2]
hhigh = stringlist[3]
shigh = stringlist[4]
vhigh = stringlist[5]
brightness = stringlist[6]

lowValues = np.array((hlow,slow,vlow))
highValues = np.array((hhigh,shigh,vhigh))

print lowValues
print highValues
print brightness
