def func(*args):
	ret_values = []
	
	from math import floor
	n = int(args[0])
	c = 1
	while ((c * 5) < n):
	    n -= (c * 5)
	    c *= 2
	exp = floor(((n - 1) / c))
	if (exp == 0):
	    ret_values.append('Sheldon')
	if (exp == 1):
	    ret_values.append('Leonard')
	if (exp == 2):
	    ret_values.append('Penny')
	if (exp == 3):
	    ret_values.append('Rajesh')
	if (exp == 4):
	    ret_values.append('Howard')

	return ret_values
