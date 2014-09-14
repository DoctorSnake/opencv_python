#!/usr/bin/env python

import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('left3.png',0)
imgR = cv2.imread('right3.png',0)

#stereo = cv2.createStereoBM(numDisparities=16, blockSize=15)
stereo = cv2.StereoBM(0, 16, 15)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()
