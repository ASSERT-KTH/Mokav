def func(*args):
	ret_values = []
	
	import sys
	(a, b) = args[0].split()
	a = int(a)
	b = int(b)
	x = (a - b)
	if ((a == 0) and (b == 0)):
	    ret_values.append('NO')
	    sys.exit()
	if (x < 0):
	    x = (- x)
	if (x > 1):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
