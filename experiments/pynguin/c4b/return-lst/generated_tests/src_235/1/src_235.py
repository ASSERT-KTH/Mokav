def func(*args):
	ret_values = []
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	i = 0
	p = 0
	for i in range((a + 1)):
	    if (((2 * i) <= b) and ((4 * i) <= c)):
	        p = i
	if (p > 0):
	    sum = ((p + (2 * p)) + (4 * p))
	else:
	    sum = 0
	ret_values.append(sum)

	return ret_values
