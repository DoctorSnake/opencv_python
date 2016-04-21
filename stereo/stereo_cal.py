#!/usr/bin/env python

import time
import numpy as np
import cv2
from matplotlib import pyplot as plt

left = []
right = []

for i in range(1,15):
	if i < 10:
		lfile = 'chessboard/left'+ '0' + str(i)
		rfile = 'chessboard/right'+ '0' + str(i)
	else:
		lfile = 'chessboard/left' + str(i)
		rfile = 'chessboard/right' + str(i)
		
	li = cv2.imread(lfile,0)
	ri = cv2.imread(rfile,0)
	
	


#plt.imshow(disparity,'gray')
#plt.show()
