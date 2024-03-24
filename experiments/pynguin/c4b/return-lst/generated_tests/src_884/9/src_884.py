def func(*args):
	ret_values = []
	
	import math
	x = int(args[0])
	n = int(math.log(((x / 5) + 1), 2))
	size = int(math.pow(2, n))
	rem = ((x - (5 * (size - 1))) - 1)
	p = (rem // size)
	if (p == 0):
	    ret_values.append('Sheldon')
	elif (p == 1):
	    ret_values.append('Leonard')
	elif (p == 2):
	    ret_values.append('Penny')
	elif (p == 3):
	    ret_values.append('Rajesh')
	else:
	    ret_values.append('Howard')

	return ret_values
