def func(*args):
	ret_values = []
	
	(even, odd) = (int(x) for x in args[0].split())
	if (abs((even - odd)) > 1):
	    ret_values.append('NO')
	elif ((even == 0) and (odd == 0)):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
