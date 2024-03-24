def func(*args):
	ret_values = []
	
	import math
	inputs = [int(x) for x in args[0].split()]
	y = inputs[0]
	k = inputs[1]
	n = inputs[2]
	result = ''
	x = (k - (y % k))
	i = x
	while ((i + y) <= n):
	    result += (str(i) + ' ')
	    i += k
	if len(result):
	    ret_values.append(result[0:(len(result) - 1)])
	else:
	    ret_values.append('-1')

	return ret_values
