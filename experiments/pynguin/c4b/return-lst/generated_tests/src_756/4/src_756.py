def func(*args):
	ret_values = []
	
	n = int(args[0])
	for i in range(20, (- 1), (- 1)):
	    if ((2 ** i) <= n):
	        ret_values.append((i + 1), end=' ')
	        n -= (2 ** i)

	return ret_values
