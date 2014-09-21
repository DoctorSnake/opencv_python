#!/usr/bin/env python

import cv2

img_width = 320
img_height = 240

# Source: 0 - built in camera  1 - USB attached camera
cap = cv2.VideoCapture(1)
ret = cap.set(3,img_width)
ret = cap.set(4,img_height)

# create a video writer to same images
#mpg4 = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
mpg4 = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter()
out.open("output.mp4v",mpg4, 20.0, (img_width,img_height))
font = cv2.FONT_HERSHEY_SIMPLEX

while(True):
	# Capture frame-by-frame 
	ret, frame = cap.read()
	#print str(ret) + '\n'
	
	if ret == True:
		#frame = cv2.circle(frame,(147,63), 30, (150,0,0), 1)
		# Our operations on the frame come here
		# for some reason cv2.COLOR_BGR2GRAY seems to crash this
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
		#cv2.circle(hsv,(147,63), 30, (50,50,30), -1)
		
		#font_scale = 1
		#font_color = (155,0,0)
		#cv2.putText(hsv, 'OpenCV',(100,100),font,font_scale,font_color,2)
		
		# Display the resulting frame
		cv2.imshow('frame',hsv)
		out.write(hsv)
	
	if cv2.waitKey(10) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows() 
