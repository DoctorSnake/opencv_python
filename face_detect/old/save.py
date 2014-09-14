#!/usr/bin/env python

import cv2
import numpy as np

img_width = 320
img_height = 240

def _R1(BGR):
	# channels
	B = BGR[:,:,0]
	G = BGR[:,:,1]
	R = BGR[:,:,2]
	e1 = (R>95) & (G>40) & (B>20) & ((np.maximum(R,np.maximum(G,B)) - np.minimum(R, np.minimum(G,B)))>15) & (np.abs(R-G)>15) & (R>G) & (R>B)
	e2 = (R>220) & (G>210) & (B>170) & (abs(R-G)<=15) & (R>B) & (G>B)
	return (e1|e2)

def _R2(YCrCb):
	Y = YCrCb[:,:,0]
	Cr = YCrCb[:,:,1]
	Cb = YCrCb[:,:,2]
	e1 = Cr <= (1.5862*Cb+20)
	e2 = Cr >= (0.3448*Cb+76.2069)
	e3 = Cr >= (-4.5652*Cb+234.5652)
	e4 = Cr <= (-1.15*Cb+301.75)
	e5 = Cr <= (-2.2857*Cb+432.85)
	return e1 & e2 & e3 & e4 & e5


def _R3(HSV):
	H = HSV[:,:,0]
	S = HSV[:,:,1]
	V = HSV[:,:,2]
	return ((H<25) | (H>230))

def detect(src):
	srcYCrCb = cv2.cvtColor(src, cv2.COLOR_BGR2YCR_CB)
	srcHSV = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
	skinPixels = (_R1(src) & _R2(srcYCrCb) & _R3(srcHSV))
	#print skinPixels
	#exit()
	h = np.asarray(skinPixels, dtype=np.uint8) * 255
	return h

# Source: 0 - built in camera  1 - USB attached camera
cap = cv2.VideoCapture(0)
ret = cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH ,img_width)
ret = cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,img_height)

# create a video writer to same images
mpg4 = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
out = cv2.VideoWriter()
out.open("output.mp4v",mpg4, 20.0, (img_width,img_height))
font = cv2.FONT_HERSHEY_SIMPLEX

while(True):
	# Capture frame-by-frame 
	ret, frame = cap.read(1)
	#print str(ret) + '\n'
	
	if ret == True:
		#frame = cv2.circle(frame,(147,63), 30, (150,0,0), 1)
		# Our operations on the frame come here
		# for some reason cv2.COLOR_BGR2GRAY seems to crash this
		#hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
		
		skin = detect(frame)
		
		#font_scale = 1
		#font_color = (155,0,0)
		#cv2.putText(hsv, 'OpenCV',(100,100),font,font_scale,font_color,2)
		
		# Display the resulting frame
		#hsv2 = _R3(hsv)
		cv2.imshow('frame',skin)
		#out.write(hsv)
	
	if cv2.waitKey(10) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows() 
