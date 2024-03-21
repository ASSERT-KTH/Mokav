def func(*args):
	ret_values = []
	
	import sys
	import math
	(x, y) = [int(x) for x in sys.stdin.readline().split()]
	while 1:
	    if ((x >= 2) and (y >= 2)):
	        x -= 2
	        y -= 2
	    elif ((x >= 1) and (y >= 12)):
	        x -= 1
	        y -= 1
	    elif ((x == 0) and (y >= 22)):
	        y -= 22
	    else:
	        ret_values.append('Hanako')
	        exit()
	    if (y >= 22):
	        y -= 22
	    elif ((x >= 1) and (y >= 12)):
	        x -= 1
	        y -= 12
	    elif ((x >= 2) and (y >= 2)):
	        x -= 2
	        y -= 2
	    else:
	        ret_values.append('Ciel')
	        exit()

	return ret_values
