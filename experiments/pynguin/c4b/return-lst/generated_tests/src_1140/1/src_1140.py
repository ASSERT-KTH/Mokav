def func(*args):
	ret_values = []
	
	(a, b, d) = [int(i) for i in args[0].split()]
	try:
	    if ((((b - a) % d) == 0) and (((b - a) / d) >= 0)):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	except:
	    if (a == b):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')

	return ret_values
