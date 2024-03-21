def func(*args):
	ret_values = []
	
	import math
	n = list(map(int, args[0].split()))
	k = (math.ceil(((n[0] * n[2]) / 100)) - n[1])
	if (k >= 0):
	    ret_values.append(k)
	else:
	    ret_values.append('0')

	return ret_values
