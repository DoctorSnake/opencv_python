#!/usr/bin/env python
#
# A python conversion of my cpp code
#
# Kevin J. Walchko
# 14 Sept 2014
#

import numpy as np
import cv2

"""
Class to unwarp omni images into a 360 degree panoramic image.
"""
class Dewarper:
	def __init__(self, Ws, Hs, Rmax, Rmin, Cx, Cy, interpolation=cv2.INTER_CUBIC):
		self.interpolation = interpolation
		
		# determine the destination image size
		Wd = int(2.0*(float(Rmax+Rmin)/2.0)*np.pi)
		Hd = Rmax-Rmin
		
		print 'Unwrapped image size:',Wd,Hd

		self.buildLUT(Wd, Hd, Rmax, Rmin, Cx, Cy)

	""" 
	Creates a polar map look up table (LUT)
	in:
		Wd - width destination
		Hd - height destination
		Ws - width src
		Hs - height src
		Rmin - inner ring of image
		Rmax - outer ring of image
		Cx - camera center x
		Cy - camera center y
	out: mapping matrix
	"""
	def buildLUT(self, Wd, Hd, Rmax, Rmin, Cx, Cy):
		map_x = np.zeros((Hd, Wd), np.float32)
		map_y = np.zeros((Hd, Wd), np.float32)
		
		# polar to Cartesian
		# x = r*cos(t)
		# y = r*sin(t)
		for i in range(0,int(Hd)):
			for j in range(0,int(Wd)):
				theta = -float(j)/float(Wd)*2.0*np.pi
				rho = float(Rmin + i)
				map_x.itemset((i,j), Cx + rho*np.cos(theta))
				map_y.itemset((i,j), Cy + rho*np.sin(theta))
				
		(self.map1, self.map2) = cv2.convertMaps(map_x, map_y, cv2.CV_16SC2)
	
	
	"""
	Takes the original image and unwarps it, note the new image is much smaller
	in: raw image needing to be unwarped
	out: panoramic image
	"""
	def unwarp(self, img):
		output = cv2.remap(img, self.map1, self.map2, self.interpolation)
		return output
