def func(*args):
	ret_values = []
	
	(n, k) = args[0].split()
	n = int(n)
	k = int(k)
	if (((n // k) % 2) == 0):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
