#!/usr/bin/python
#
# This is a simple little server that displays a webpage. Note it only delivers
# one webpage or any css or any js files you need.
#
# copyright Kevin Walchko
# 29 July 2014
#

import time
import json
import cv2
import base64
import numpy
from multiprocessing.connection import Client as Subscriber


if __name__ == '__main__':
	s = Subscriber(("localhost",8080))
	for i in range(1,1000):
#		try:
			im = s.recv()
			im = base64.b64decode(im)
			im = numpy.fromstring(im,dtype=numpy.uint8)
			buf = cv2.imdecode(im,1)
			cv2.imshow('girl',buf)
			cv2.waitKey(10)
			#json_data = s.recv()
			#data = json.loads(json_data)
			#data['bob'] += 1;
		
			#pkg = json.dumps( data )
			#s.send(pkg)
# 		except:
# 			print "Error"
		
	s.close()
	
    