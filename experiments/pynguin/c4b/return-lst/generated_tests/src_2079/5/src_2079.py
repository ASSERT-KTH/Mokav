def func(*args):
	ret_values = []
	
	import sys
	m = int(args[0])
	if ((((m - 2) % 2) == 0) and (m > 2)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
