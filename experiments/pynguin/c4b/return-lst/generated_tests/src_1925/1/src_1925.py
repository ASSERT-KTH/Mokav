def func(*args):
	ret_values = []
	
	import math
	import sys
	(a, b) = args[0].split()
	a = int(a)
	b = int(b)
	if ((a == 0) and (b == 0)):
	    ret_values.append('NO')
	    sys.exit()
	if (a >= b):
	    if ((a - b) > 1):
	        ret_values.append('NO')
	    else:
	        ret_values.append('YES')
	elif ((b - a) > 1):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
