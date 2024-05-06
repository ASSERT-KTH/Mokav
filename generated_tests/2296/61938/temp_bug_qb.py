def original_func(*args):
	global_list = []
	
	import math
	dimension = args[0]
	dim = dimension.split()
	M = math.floor(int(dim[0]))
	N = math.floor(int(dim[1]))
	if ((M % 2) == 1):
	    global_list.append(str(((((M - 1) / 2) * N) + (N / 2))))
	else:
	    global_list.append(str(((M / 2) * N)))
	return global_list