def func(*args):
	ret_values = []
	
	import math
	n = int(args[0])
	v = math.floor((((- 1) + math.sqrt((1 + (8 * n)))) / 2))
	for i in range(v, 0, (- 1)):
	    z = (n - ((i * (i + 1)) / 2))
	    a = (((- 1) + math.sqrt((1 + (8 * z)))) / 2)
	    if (a.is_integer() and (a > 0)):
	        ret_values.append('YES')
	        exit(0)
	ret_values.append('NO')

	return ret_values
