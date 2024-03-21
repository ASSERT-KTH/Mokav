def func(*args):
	ret_values = []
	
	import math
	data = args[0].split()
	(N, X, Y) = (int(data[0]), int(data[1]), int(data[2]))
	clones = (math.ceil((N * (Y / 100))) - X)
	if (clones > 0):
	    ret_values.append(clones)
	else:
	    ret_values.append(0)

	return ret_values
