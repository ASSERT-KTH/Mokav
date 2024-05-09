def original_func(*args):
	global_list = []
	
	import math
	inputs = [int(x) for x in args[0].split()]
	y = inputs[0]
	k = inputs[1]
	n = inputs[2]
	result = ''
	x = (k - (y % k))
	i = x
	while ((i < n) and ((i + y) < n)):
	    result += (str(i) + ' ')
	    i += k
	if len(result):
	    global_list.append(result[0:(len(result) - 1)])
	else:
	    global_list.append('-1')
	return global_list