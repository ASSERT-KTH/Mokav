def func(*args):
	ret_values = []
	
	import sys
	(a, b) = [int(x) for x in args[0].split()]
	if ((a == 0) and (b == 0)):
	    ret_values.append('NO')
	    sys.exit()
	if (a == b):
	    ret_values.append('YES')
	    sys.exit()
	if (a > b):
	    if ((a - b) == 1):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	elif ((b - a) == 1):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
