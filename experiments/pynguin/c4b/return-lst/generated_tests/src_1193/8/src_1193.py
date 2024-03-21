def func(*args):
	ret_values = []
	
	import sys
	x = list(map(int, sys.stdin.readline().split()))
	vmax = 0
	vmin = 100
	for i in x:
	    if (i < vmin):
	        vmin = i
	    if (i > vmax):
	        vmax = i
	ret_values.append((vmax - vmin))

	return ret_values
