def func(*args):
	ret_values = []
	
	n = int(args[0])
	x = 0
	for j in range(2, n):
	    x = (x + ((n - j) * j))
	ret_values.append((((x + n) - 1) + n))

	return ret_values
