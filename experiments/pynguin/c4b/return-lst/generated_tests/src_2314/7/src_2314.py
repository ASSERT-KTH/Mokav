def func(*args):
	ret_values = []
	
	import math
	dimension = args[0]
	dim = dimension.split()
	M = math.floor(int(dim[0]))
	N = math.floor(int(dim[1]))
	if ((M % 2) == 1):
	    ret_values.append(int(((((M - 1) / 2) * N) + (N / 2))))
	else:
	    ret_values.append(int(((M / 2) * N)))

	return ret_values
