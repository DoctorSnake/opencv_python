#!/usr/bin/env python

import argparse

# create parser
parser = argparse.ArgumentParser('This is a test program for argparse. It does nothing of value')

# add args with default values
parser.add_argument('-c', '--camera', help='which camera to use', default=0)
parser.add_argument('-f', '--file', help='save calibration values', default='cal_data.npy')

# add mandatory args
parser.add_argument('--loop', help='how long do we loop for', required=True)

# check args, make dict using var()
args = vars(parser.parse_args())

# see command line args passed or defaults
print args['camera']
print args['file']
print args['loop']

print '**********************'
print '*       Done         *'
print '**********************'

