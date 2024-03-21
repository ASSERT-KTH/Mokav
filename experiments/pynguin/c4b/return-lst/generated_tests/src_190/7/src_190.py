def func(*args):
	ret_values = []
	
	import math
	(n, k) = map(int, args[0].split())
	if (((n // k) & 1) == 1):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
