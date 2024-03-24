def func(*args):
	ret_values = []
	
	n = args[0]
	ret_values.append([n, n.swapcase()][(n[1:] == n[1:].upper())])

	return ret_values
