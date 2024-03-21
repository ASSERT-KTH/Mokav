def func(*args):
	ret_values = []
	
	n = int(args[0])
	l = 0
	for i in range(1, n):
	    l += (i * (n - i))
	ret_values.append((l + n))

	return ret_values
