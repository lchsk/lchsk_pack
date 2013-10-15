
import sys
import os
import math
from PIL import Image

def read_settings():
	#args = sys.argv[1:]

	args = {}

	# parameters to set
	args['input_folder'] = 'bernitems'
	args['output_file']  = 'output.png'
	args['out_w'] = 1024
	args['out_h'] = 1024
	args['in_w'] = 70
	args['in_h'] = 70
	args['avai'] = {}
	args['im'] = None
	args['files'] = []
	
	return args

def init(args):
	for i in xrange(0, args['out_h'] - args['in_h'], args['in_h']):
		for j in xrange(0, args['out_w'] - args['in_w'], args['in_w']):
			args['avai'][(i, j)] = True

	args['im'] = Image.new("RGBA", (args['out_w'], args['out_h']), None)

	args['files'] = os.listdir(args['input_folder'])
	
def get_places_list(args, start, w, h):
	ret_list = []
	
	for j in range(start[0], start[0] + int(w), args['in_w']):
		for i in range(start[1], start[1] + int(h), args['in_h']):
			ret_list.append((i, j))
	
	return ret_list

def check_list(args, places_list):
	for el in places_list:
		if el not in args['avai'] or not args['avai'][el]:
			return False
	return True

def mark_list(args, places_list):
	for el in places_list:
		args['avai'][el] = False

def get_next_free(args, size, what):
		
	if what == 'any':
		for place in args['avai']:
			if args['avai'][place]:
				return place
	else:		
		w = math.ceil(float(size[0]) / args['in_w'])
		h = math.ceil(float(size[1]) / args['in_h'])
		
		wspace = w * args['in_w']
		hspace = h * args['in_h']
		
		for place in args['avai']:
			if check_list(args, get_places_list(args, place, wspace, hspace)):
				mark_list(args, get_places_list(args, place, wspace, hspace))
				return place
		
	return None

def merge_files(args):
	for f in args['files']:
		#try:
			img = Image.open(args['input_folder'] + '/' + f)
			print '\nloaded ' + f
			
			
			#pos = find_pos(args, img.size)
			pos = get_next_free(args, img.size, 'big')
			print pos
			
			#if pos is not None:
		#		args['avai'][pos] = False
			#print pos
			
			args['im'].paste(img, pos, img)	
			
		#except:
		#	print 'Something wrong with ' + f

	args['im'].save(args['output_file'])

def main():
	
	args = read_settings()
	init(args)
	
	print (0,0) in args['avai']
	
	merge_files(args)

if __name__ == '__main__':
	main()



