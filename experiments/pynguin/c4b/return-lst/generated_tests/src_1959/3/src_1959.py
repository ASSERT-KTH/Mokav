def func(*args):
	ret_values = []
	
	(n, k) = map(int, args[0].split())
	x = ((3 * n) - k)
	if (x <= 0):
	    ret_values.append('0')
	else:
	    ret_values.append(x)

	return ret_values
