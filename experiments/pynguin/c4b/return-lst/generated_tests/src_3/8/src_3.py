def func(*args):
	ret_values = []
	
	n = int(args[0])
	a = [0, 1]
	while (a[(- 1)] < n):
	    a += [((a[(- 1)] + a[(- 2)]) + 1)]
	ret_values.append((len(a) - 2))

	return ret_values
