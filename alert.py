#!/usr/bin/python
import cv2
import numpy as np
from scipy.misc import imread, imresize, imsave
import time
from matplotlib import pyplot as plt
import subprocess

# Read image
subprocess.call('avconv -loglevel fatal -i "rtmp://192.168.1.22:1935" -r 1 -vframes 1 original.jpg', shell=True)
img = imread("original.jpg")
img = imresize(img, (480,640))
color_min = (1,1,1)
color_max = (255,255,255)
count = 0
while True:
    print 'Retrieving image...'
    subprocess.call('avconv -loglevel fatal -i "rtmp://192.168.1.22:1935" -r 1 -vframes 1 new.jpg', shell=True)
    img2 = imread("new.jpg")
    img2 = imresize(img2, (480,640))
    im = cv2.absdiff(img,img2)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    im = cv2.inRange(im, color_min, color_max)
    white_pixels = cv2.countNonZero(im)
    print white_pixels
    if white_pixels is not 0:
	img = img2
#	imsave('original.jpg', img)
	print 'Alert!'
    else: 
	pass
