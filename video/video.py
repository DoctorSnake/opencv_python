#! /usr/bin/env python

import numpy as np
import cv2


img_width = 640
img_height = 480


cap = cv2.VideoCapture(0)

ret = cap.set(3,img_width)
if not ret: print 'WARNiNG: Could not set image width to',img_width

ret = cap.set(4,img_height)
if not ret: print 'WARNiNG: Could not set image height to',img_height

#fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
fourcc = cv2.cv.FOURCC('m', 'p', '4', 'v')
out = cv2.VideoWriter('output.mp4',fourcc, 30, (img_width,img_height),True)

count = 0
while(cap.isOpened()):
	count = count + 1
	print "processing frame ", count
	ret, frame = cap.read()
	if ret: out.write(frame)
	
	if cv2.waitKey(10) and 0xFF == ord('q'):
		break


cap.release()
out.release()
cv2.destroyAllWindows()