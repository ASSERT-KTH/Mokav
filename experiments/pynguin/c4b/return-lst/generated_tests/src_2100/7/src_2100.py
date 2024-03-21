def func(*args):
	ret_values = []
	
	(n, k) = args[0].split(' ')
	if (((int(n) // int(k)) % 2) == 0):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
