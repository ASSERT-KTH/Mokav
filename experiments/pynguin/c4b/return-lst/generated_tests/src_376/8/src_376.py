def func(*args):
	ret_values = []
	
	n = args[0]
	if (((int(n) % 2) == 1) or (int(n) <= 2)):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
