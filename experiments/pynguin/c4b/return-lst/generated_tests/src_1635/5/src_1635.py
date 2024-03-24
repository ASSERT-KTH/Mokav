def func(*args):
	ret_values = []
	
	n = int(args[0])
	tot = 0
	for i in range(1, (n + 1)):
	    tot += (2 ** i)
	ret_values.append(tot)

	return ret_values
