# USAGE
# python pi_robot_alarm --picamera if the picamera is being used
# import the necessary packages
from __future__ import print_function
from imutils.video import VideoStream
from gpiozero import CamJamKitRobot, LED 
#import Robot if you're using another controller board or import the library provided by your board
import argparse
import imutils
import time
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--picamera", type=int, default=-1,
	help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())

# initialize the video stream and allow the cammera sensor to
# warmup
print("[INFO] waiting for camera to warmup...")
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)

# define the lower and upper boundaries of the "green"
# ball in the HSV color space
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

# initialize the Robot and LED and whether or not the Robot is on
# If using another controller board here is an example of how to set it up
# robot = Robot(left=(4, 14), right=(23, 24)) if using pins 4, 14 for left and 23 and 24 for right
devastator_robot = CamJamKitRobot()
robotOn = False
devastator_eye = LED(25)

#Flash the LED 4 times to ensure the code is running
for x in range(1, 5):
	devastator_eye.off()
	time.sleep(0.5)
	devastator_eye.on()
	time.sleep(0.5)

# loop over the frames from the video stream
while True:
	# grab the next frame from the video stream, resize the
	# frame, and convert it to the HSV color space
	frame = vs.read()
	frame = imutils.resize(frame, width=500)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	center = None

	# only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		# only proceed if the radius meets a minimum size
		if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)

			# if the robot is not already on, turn it on
			# and switch the variable to True
			if not robotOn:
				devastator_robot.forward()
				robotOn = True

	# if the ball is not detected, turn off the robot and now set it to False
	elif robotOn:
		devastator_robot.stop()
		robotOn = False

	# show the frame to our screen
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
devastator_eye.off()
devastator_robot.off()
