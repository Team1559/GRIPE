
import cv2
import numpy as np
import sys
import thread


class CameraFeed(object):

    def __init__(self):

        #create the webcam
        global cam
        cam = cv2.VideoCapture(1)
        #cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
        #cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
        cam.set(3, 640)
        cam.set(4, 480)

        #put values in for original image
        self.putLowerRange(0,0,0,)
        self.putUpperRange(255,255,255)

        #run it in a new thread
        thread.start_new_thread(self.run, ())

    def run(self):

        #start processing with the camera
        while True:

            cam.set(10, brightness) #changes the brightness

            #open the camera stream
            global frame
            _,frame = cam.read()

            #convert to hsv with supplied values
            global hsv, thresh
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            thresh = cv2.inRange(hsv, lowRange, upperRange)

            #show the feed
            cv2.imshow("GRIPE Image", thresh)
            cv2.waitKey(1)


    def putLowerRange(self, h, s, v):

        global lowRange,hlow,slow,vlow
        lowRange = np.array((h,s,v))
        hlow = h
        slow = s
        vlow = v


    def putUpperRange(self, h, s, v):

        global upperRange,hhigh,shigh,vhigh
        upperRange = np.array((h,s,v))
        hhigh = h
        shigh = s
        vhigh = v


    def putBrightness(self, num):

        global brightness
        brightness = num


    def writeImage(self):

        if path == "" or path == "Image Save Path":
            return  #No Path Found
        else:
            cv2.imwrite(path, thresh)


    def writeFile(self):

        with open(path+"/config.gripe", 'w') as f:
            f.write(str(hhigh)+"\n"+str(shigh)+"\n"+str(vhigh)+"\n"+str(hlow)+"\n"+str(slow)+"\n"+str(vlow)+"\n"+str(brightness))


    def setPath(self, string):

        global path
        path = string
