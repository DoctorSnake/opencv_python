#!/usr/bin/env python

import numpy as np
import cv2
import glob
import yaml

mtx = np.array([[ 532.80990646 ,0.0,342.49522219],[0.0,532.93344713,233.88792491],[0.0,0.0,1.0]])
dist = np.array([-2.81325798e-01,2.91150014e-02,1.21234399e-03,-1.40823665e-04,1.54861424e-01])

data = {'camera_matrix': mtx, 'dist_coeff': dist}

#print mtx
#print dist
print data

fd = open('data.yaml',"w")

yaml.dump(data,fd)
fd.close()

# read back in
fd = open('data.yaml',"r")
data2 = yaml.load(fd)
#data2 = np.array(data2)
mtx2 = data2['camera_matrix']
#dist2 = data2['dist_coeff']
#fd.close()

print "\n\n"
print data2
print mtx2