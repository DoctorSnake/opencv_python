#!/usr/bin/env python

import numpy as np
import cv2
import glob
import yaml

def saveFile(fname,data):
	fd = open(fname,"w")
	yaml.dump(data,fd)
	fd.close()

def readFile(fname):
	fd = open(fname,"r")
	data = yaml.load(fd)
	return data

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all the images. 
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('chessboard/*.jpg')

for fname in images:
	img = cv2.imread(fname)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	
	# Find the chess board corners
	ret, corners = cv2.findChessboardCorners(gray, (7,6),None)
	#print corners
	#ret, corners = cv2.findCirclesGrid(gray, (7,6),None)
	
	# If found, add object points, image points (after refining them)
	if ret == True: 
		objpoints.append(objp)
		#corners2 = corners
		#cv2.cornerSubPix(gray,corners2,(11,11),(-1,-1),criteria)
		#print (corners2-corners)
		imgpoints.append(corners)
		# Draw and display the corners
		cv2.drawChessboardCorners(img, (7,6), corners,ret)
		cv2.imshow('img',img)
		cv2.waitKey(500)
		
#, rvecs, tvecs
#mtx = [[]]
#dist = []
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
#ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],rvecs,tvecs)


img = cv2.imread('chessboard/left12.jpg')
h,  w = img.shape[:2]
newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))




print 'Original Matricies: '
print mtx
print dist
print newcameramtx
print '\n---------------\n'



data = {'camera_matrix': mtx, 'dist_coeff': dist, 'newcameramtx': newcameramtx}

# save data to file
saveFile('calibration.npy',data)

# read back in
data = readFile('calibration.npy')

mtx = data['camera_matrix']
dist = data['dist_coeff']
newcameramtx = data['newcameramtx']

print 'read back in:'
print mtx
print dist
print newcameramtx

# undistort
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

# crop the image
x,y,w,h = roi
# crop the distorted edges off
#dst = dst[y:y+h, x:x+w]
cv2.imwrite('calibresult.png',dst)

cv2.imshow('calibrated image',dst)
cv2.waitKey(0)

cv2.destroyAllWindows()