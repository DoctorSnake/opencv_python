#!/usr/bin/env python
#
# To do:
# - pass image list from command line
# - pass checkerboard or circles from command line
# - pass save file name from command line
# - pass cal images grab live or from file

import numpy as np
import cv2
import glob
import yaml

# temp globals ----------------------
save_file = 'calibration.npy'
calibration_images = 'chessboard/*.jpg'
marker_size = (9,6) #(11,4) #(7,6)
get_images_live = True
marker_checkerboard = True
camera_num = 0

# Globals ----------------------------
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((marker_size[0]*marker_size[1],3), np.float32)
objp[:,:2] = np.mgrid[0:marker_size[0],0:marker_size[1]].T.reshape(-1,2)

g_image = []

# Arrays to store object points and image points from all the images. 
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

# write camera calibration file out
def saveFile(fname,data):
	fd = open(fname,"w")
	yaml.dump(data,fd)
	fd.close()

# read camera calibration file in
def readFile(fname):
	fd = open(fname,"r")
	data = yaml.load(fd)
	return data

# Pass a gray scale image and find the markers (i.e., checkerboard, circles)
def findMarkers(gray):
	# Find the chess board corners
	if marker_checkerboard == True:
		ret, corners = cv2.findChessboardCorners(gray, marker_size,None)
		print 'chess - found corners: ' + str(corners.size) + ' ' + str(ret)
	else:
		ret, corners = cv2.findCirclesGridDefault(gray, marker_size,None,cv2.CALIB_CB_ASYMMETRIC_GRID)
		print 'circles - found corners: ' + str(corners.size) + ' ' + str(ret)
		print corners

	# If found, add object points, image points (after refining them)
	if ret == True: 
		objpoints.append(objp)
		#corners2 = corners
		#cv2.cornerSubPix(gray,corners2,(11,11),(-1,-1),criteria)
		#print (corners2-corners)
		imgpoints.append(corners)
		
		# Draw and display the corners
		cv2.drawChessboardCorners(gray, marker_size, corners,ret)
		cv2.imshow('camera',gray)
		cv2.waitKey(500)
	else:
		print 'Couldn\'t find markers'
		
	return ret


def main():
	# termination criteria
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
	images = []

	if get_images_live == True:
		cap = cv2.VideoCapture(camera_num)
		image_cnt = 0
		
		# grab images
		while image_cnt < 5:
			ret, frame = cap.read()
			if ret == True:
				cv2.imshow('camera',frame)
			key = cv2.waitKey(30)
			
			#print str(key) + ' ' + str(ret)
			
			if key == ord('q'):
				exit(0)
			
			if key == ord('g') and ret == True:
				gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
				cv2.imshow('camera', gray)
				ret = findMarkers(gray)
				if ret == True: 
					image_cnt += 1
					print 'Found markers: ' + str(image_cnt)
					g_image = frame
	else:
		images = glob.glob(calibration_images)

		for fname in images:
			img = cv2.imread(fname)
			gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
			ret = findMarkers(gray)
			g_image = img
			
	ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

	h,  w = g_image.shape[:2]
	newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

	data = {'camera_matrix': mtx, 'dist_coeff': dist, 'newcameramtx': newcameramtx}

	# save data to file
	saveFile(save_file,data)
	
	cv2.destroyWindow('camera')
	
	#-----------------------------------------------------------------
	
	# read back in
	data = readFile(save_file)

	mtx = data['camera_matrix']
	dist = data['dist_coeff']
	newcameramtx = data['newcameramtx']

	# undistort
	dst = cv2.undistort(g_image, mtx, dist, None, newcameramtx)

	# crop the image
	x,y,w,h = roi
	# crop the distorted edges off
	#dst = dst[y:y+h, x:x+w]
	cv2.imwrite('calibresult.png',dst)

	cv2.imshow('calibrated image',dst)
	cv2.imshow('original image', g_image)
	cv2.waitKey(0)

	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()