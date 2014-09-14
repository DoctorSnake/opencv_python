#!/usr/bin/env python

import cv2

cap = cv2.VideoCapture(1)
ret = cap.set(3,320)
ret = cap.set(4,240)

while(True):
	# Capture frame-by-frame 
	ret, frame = cap.read()
	# Our operations on the frame come here
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	# Display the resulting frame
	cv2.imshow('frame',gray)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows() 
