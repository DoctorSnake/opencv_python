#! /usr/bin/env python

import numpy as np
import cv2
import time

imgs = []

for i in range(1,6):
	file = 'stitching_img/S%d.jpg'%i
	print file
	im = cv2.imread(file)
	imgs.append(im)

# for i in imgs:
# 	cv2.imshow('image',i)
# 	cv2.waitKey(100)
	

st=cv2.createStitcher()
ret,pano = st.stitch(imgs)

print 'ret',ret

if ret: cv2.imwrite('pano.png',pano)

#cv2.imshow('image',pano)
#cv2.waitKey(2000)

#cv2.destroyAllWindows()