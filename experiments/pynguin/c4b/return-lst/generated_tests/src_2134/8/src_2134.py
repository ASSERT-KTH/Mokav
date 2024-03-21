def func(*args):
	ret_values = []
	
	inp = int(args[0])
	d = 1
	c = 0
	for i in range(0, (inp - 1)):
	    d += (i + 1)
	    if ((d % inp) == 0):
	        c = inp
	    else:
	        c = (d % inp)
	    ret_values.append(c, end=' ')

	return ret_values
