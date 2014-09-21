#!/usr/bin/env python

import cv2

cap = cv2.VideoCapture(1)
#ret = cap.set(3,320)
#ret = cap.set(4,240)

ret, frame = cap.read()
h,w,d = frame.shape

print 'Image size:',w,h

while(True):
	# Capture frame-by-frame 
	ret, frame = cap.read()
	# Our operations on the frame come here
	#gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
# 	cx = w/2-40
# 	cy = h/2+20
# 	rmax = 315
# 	rmin = 150
	
	cx = w/2-15
	cy = h/2+5
	rmax = 315
	rmin = 150
	
	cv2.circle(frame,(cx,cy),10,(0,250,0),-1)
	cv2.circle(frame,(cx,cy),rmax,(0,0,250),1)
	cv2.circle(frame,(cx,cy),rmin,(250,0,0),1)
	
	# Display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows() 
