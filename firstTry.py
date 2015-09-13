#########
# firstTry.py
# This program is part of the online PS-Drone-API-tutorial on www.playsheep.de/drone.
# It shows how to do basic movements with a Parrot AR.Drone 2.0 using the PS-Drone-API.
# Dependencies: a POSIX OS, PS-Drone-API 2.0 beta or higher.
# (w) J. Philipp de Graaff, www.playsheep.de, 2014
##########
# LICENCE:
#   Artistic License 2.0 as seen on http://opensource.org/licenses/artistic-license-2.0 (retrieved December 2014)
#   Visit www.playsheep.de/drone or see the PS-Drone-API-documentation for an abstract from the Artistic License 2.0.
###########

import time, sys
import ps_drone                # Imports the PS-Drone-API
import numpy as np
import argparse
import cv2
import os
from os import listdir

imgCount = 0
peopleToRescue = []

picList = [f for f in listdir("./") if (os.path.splitext(f)[1] == ".png")]
picList.sort()

def userPrompt():
	input = raw_input("Continue? ")
	if input == "y":
		return 0
	else:
		drone.stop()
		drone.land()
		print "%d people to rescue" %(len(listdir("./")))
		#for people in peopleToRescue:
			#image = cv2.imread(pic)
			#cv2.imshow("survivors",np.hstack([image]))
 
		exit()

def processImage(imgNumber):
	global picList
	global imgCount
	pic = picList[imgNumber]
	image = cv2.imread(pic)
	height, width = image.shape[:2]
	blank = np.zeros((height, width, 3), np.uint8)

	boundaries = [
#        	([10, 50, 200], [50, 120, 240])
		([0, 50, 150], [50, 255, 255])
	]

	for(lower, upper) in boundaries:
        	lower = np.array(lower, dtype = "uint8")
        	upper = np.array(upper, dtype = "uint8")

		converted = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        	skinMask = cv2.inRange(converted, lower, upper)
		kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
		skinMask = cv2.erode(skinMask, kernel, iterations = 2)
		skinMask = cv2.dilate(skinMask, kernel, iterations = 2)

		skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
		output = cv2.bitwise_and(image, image, mask = skinMask)

	imgCount += 1
	if output.any():
		cv2.imwrite("processed_images/rescue_%s.png" %(os.path.splitext(pic)[0]), output)
		print "Survivor found in location %s" %(pic)
		#cv2.imshow("images", np.hstack([image,output]))
      		#cv2.waitKey(32)
	#else:
	#        print "No humans detected"

drone = ps_drone.Drone()       # Initializes the PS-Drone-API
drone.startup()                # Connects to the drone and starts subprocesses

while(drone.getBattery()[0]==-1):
	time.sleep(0.1)
print "Battery: " + str(drone.getBattery()[0]) + "% " + str(drone.getBattery()[1])
drone.useDemoMode(False)
drone.getNDpackage(["demo",  "wifi", "vision"])
time.sleep(0.5)

NDC = drone.NavDataCount

print "Aptitude " + str(drone.NavData["demo"][2])
print "Wifi " + str(drone.NavData["wifi"])

#CDC = drone.ConfigDataCount
#drone.setConfigAllID()
#drone.slowVideo()
#drone.frontCam()
#while CDC == drone.ConfigDataCount:
#	time.sleep(0.001)
#print "Video start"

#drone.startVideo()
#drone.showVideo()

drone.takeoff()                # Drone starts
print "I'm up"
time.sleep(7.5)                # Gives the drone time to start

print "Going on patrol"
drone.moveForward()            # Drone flies forward...
time.sleep(2)                  # ... for two seconds
drone.stop()                   # Drone stops...
time.sleep(0.5)                # ... needs, like a car, time to stop
drone.turnLeft()
time.sleep(2.3)
drone.stop()

print "Processing image %d" %(imgCount+1)
peopleToRescue.append(processImage(imgCount))
userPrompt()

print "Continue search"
drone.turnRight()	       # Drone flies backward with a quarter speed...
time.sleep(3.4)                # ... for one and a half seconds
drone.stop()                   # Drone stops

print "Processing image %d" %(imgCount+1)
peopleToRescue.append(processImage(imgCount))
userPrompt()

drone.turnRight()
time.sleep(2.8)
drone.stop()

print "Processing image %d" %(imgCount+1) 
peopleToRescue.append(processImage(imgCount))
userPrompt()

drone.turnRight()
time.sleep(2.5)
drone.stop()

print "Processing image %d" %(imgCount+1) 
peopleToRescue.append(processImage(imgCount))
userPrompt()

drone.turnLeft()
time.sleep(5)
drone.stop()

print "Processing image %d" %(imgCount+1) 
peopleToRescue.append(processImage(imgCount))
userPrompt()

print "Moving on"
drone.turnLeft()
time.sleep(4)
drone.stop()
drone.moveForward()
time.sleep(1.2)
drone.stop()
drone.turnLeft()
time.sleep(2.6)
drone.stop()

print "Processing image %d" %(imgCount+1) 
peopleToRescue.append(processImage(imgCount))
userPrompt()

drone.turnLeft()
time.sleep(2.2)
drone.stop()

print "Processing image %d" %(imgCount+1) 
peopleToRescue.append(processImage(imgCount))
userPrompt()

drone.turnLeft()
time.sleep(2.4)
drone.stop()

print "Processing image %d" %(imgCount+1) 
peopleToRescue.append(processImage(imgCount))
userPrompt()

drone.turnRight()
time.sleep(3.2)
drone.stop()

print "Processing image %d" %(imgCount+1) 
peopleToRescue.append(processImage(imgCount))
userPrompt()

drone.moveUp()
time.sleep(5)
drone.stop()
drone.turnLeft()
time.sleep(3.6)
drone.stop()
drone.moveRight()
time.sleep(3)
drone.stop()

print "Processing image %d" %(imgCount+1) 
peopleToRescue.append(processImage(imgCount))
userPrompt()

drone.turnLeft(2.4)
drone.stop()

print "Processing image %d" %(imgCount+1) 
peopleToRescue.append(processImage(imgCount))
userPrompt()

drone.moveForward()
time.sleep(1)
drone.turnLeft(2)
time.sleep(6)
drone.land()

#drone.turnLeft()               # Drone moves full speed to the left...
#time.sleep(1)                  # ... for two seconds
#drone.turnRight()
#time.sleep(1)
#drone.stop()                   # Drone stops
#time.sleep(1)

#drone.land()                   # Drone lands
