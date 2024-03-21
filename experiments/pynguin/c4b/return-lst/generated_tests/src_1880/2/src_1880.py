def func(*args):
	ret_values = []
	
	(n, k) = [int(f) for f in args[0].split()]
	if (((n // k) % 2) == 1):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
