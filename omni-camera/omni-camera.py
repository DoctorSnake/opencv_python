#!/usr/bin/env python

import sys
import cv2
import Dewarp

def initSave(filename,img_width,img_height):
	# create a video writer to same images
	#mpg4 = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
	mpg4 = cv2.VideoWriter_fourcc('M', 'P', '4', '2')
	out = cv2.VideoWriter()
	#out.open(filename,mpg4, 20.0, (img_width,img_height))
	out.open(filename,mpg4, 20.0, (640,480))
	return out

def main(camera_num):
	capture = cv2.VideoCapture(camera_num)
	retval,im = capture.read()
	
	h,w,d = im.shape
	rmax = 315
	rmin = 150
	cx = w/2-15
	cy = h/2+5
	
	save_movie = False
	movie = initSave('out.mp4v',w,h)
	
	dewarper = Dewarp.Dewarper(w,h,rmax,rmin,cx,cy)
	
	im_cnt = 0
	
	while True:
		(retval, im) = capture.read()
		
		if retval is True:
			frame = dewarper.unwarp(im)
			cv2.imshow("preview", frame)
						
			if save_movie:
				gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
				#movie.write(im)
				#print 'w'
			
			key = cv2.waitKey(10)
			if key & 0xFF == ord('q') or key == 0x1b: # ESC
				break
			elif key == ord('s'):
				#save_movie = not save
				#print 'saving file:',save_movie
				print '[!] Saving is currently disabled'
			elif key == ord('g'):
				im_cnt += 1
				cv2.imwrite('images/image_'+str(im_cnt)+'.png',frame)
				
				
		else:
			print '[-] Error reading camera'
	
	capture.release()
	movie.release()
	cv2.destroyAllWindows()
	print 'bye ...'

if __name__ == "__main__":
	main(1)
