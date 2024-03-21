def func(*args):
	ret_values = []
	
	import math
	N = int(args[0].split()[0])
	if (N % 2):
	    ret_values.append(int(((N - 1) / 2)))
	else:
	    ret_values.append(int(((N - pow(2, int(math.log2(N)))) / 2)))

	return ret_values
