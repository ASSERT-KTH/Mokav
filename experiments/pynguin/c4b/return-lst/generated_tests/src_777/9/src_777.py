def func(*args):
	ret_values = []
	
	data = [int(x) for x in args[0].split()]
	p = (data[0] - data[1])
	pf = (((data[0] - data[1]) - 1) - data[2])
	if (pf <= 0):
	    pf = 0
	ret_values.append((p - pf))

	return ret_values
