#!/usr/bin/env python

import cv2
import Dewarp as dwp


def process(file):
	# read in the image grayscale
	frame = cv2.imread(file,0)
	h,w = frame.shape
	print 'Image size:',w,h

	# These are done by hand ... had trouble automating it reliably
	cx = 1375
	cy = 870
	rmax = 578
	rmin = 250

	print 'Parameters: center(x,y) %d,%d radius(max,min) %d,%d'%(cx,cy,rmax,rmin)

	dewarp = dwp.Dewarper(w,h,rmax,rmin,cx,cy)

	cv2.circle(frame,(cx,cy),10,(0,250,0),-1)
	cv2.circle(frame,(cx,cy),rmax,(0,0,250),1)
	cv2.circle(frame,(cx,cy),rmin,(250,0,0),1)

	# Display the resulting frame
	# cv2.imshow('frame',frame)
	# cv2.waitKey(0)

	im = dewarp.unwarp(frame)
	# Display the resulting frame
	# cv2.imshow('frame',im)
	# cv2.waitKey(0)
	cv2.imwrite('picamera/image.png',im)

	# When everything done, release the capture
	cv2.destroyAllWindows()

if __name__ == "__main__":
	process('picamera/pan1.jpg')
