def func(*args):
	ret_values = []
	
	import math
	(n, k) = map(int, args[0].split())
	s = int((n // k))
	if ((s % 2) != 0):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
