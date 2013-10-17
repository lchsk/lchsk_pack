#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import os
import math
from PIL import Image


def get_input():
	params = sys.argv[1:]
	
	if len(params) is not 3:
		print 'Usage: \n\t' + sys.argv[0] + ' filename rows_n cols_n'
		
		exit(1)
	else:
		return params
		
def divide(params):
	img = Image.open(str(params[0]))
	rows = int(params[1])
	cols = int(params[2])
	
	# extension of output files
	out_ext = os.path.splitext(params[0])[1]
	
	# create output folder
	out_dir = os.path.splitext(params[0])[0]
	file_name = os.path.basename(os.path.normpath(out_dir))
	if not os.path.exists(out_dir):
		os.makedirs(out_dir)
	
	# base image size
	w, h = img.size
	
	# size of single images
	img_w = w / cols
	img_h = h / rows
	
	rows_i = w / img_w
	cols_i = h / img_h
	
	for i in xrange(0, cols_i):
		for j in xrange(0, rows_i):
			image_path = out_dir + '/' + file_name + '_'  + str(i) + str(j) + out_ext
			
			#print image_path
			
			new_img = Image.new("RGBA", (img_w, img_h))
			
			x, y, w, h = (j * img_w, i * img_h, img_w, img_h)
			box = (x, y, x + w, y + h)
			region = img.crop(box)
			
			new_img.paste(region, (0, 0))	
			new_img.save(image_path)


def main():
	divide(get_input())


if __name__ == '__main__':
	main()
