import os, re

filename = raw_input('file to parse :')


re_area_format = r'Area Size : (?P<width>\d+) x (?P<height>\d+); Area Step : (?P<step_x>\d+(.?,?\d*)?) um x (?P<step_y>\d+(.?,?\d*)?) um'

file_out = open(os.path.splitext(filename)[0] + '_parsed.txt', 'w')
with open(filename, 'r') as file_in:
	data = False
	width  = 0
	height = 0
	nb_lines = 0
	for line in file_in.readlines():
         
		m = re.search(re_area_format, line)
          
		if data :
			line_data = re.sub(',', '.', line).split('\t')
			if len(line_data) != width: raise Exception('incorrect data width')
			file_out.write('\t'.join(map(lambda x : 'nan' if x == '' else x, line_data)))
			nb_lines += 1
		if m is not None : data = True; width = int(m.group('width')); height = int(m.group('height'))
	if nb_lines != height: raise Exception('incorrect data height')
file_out.close()
