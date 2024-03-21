def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	if ((n != 0) and (m != 0)):
	    ret_values.append(max(m, n), ((n - 1) + m))
	elif (m == 0):
	    ret_values.append(n, n)
	else:
	    ret_values.append('Impossible')

	return ret_values
