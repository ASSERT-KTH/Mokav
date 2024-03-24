def func(*args):
	ret_values = []
	
	(a, b) = [int(x) for x in args[0].split()]
	if ((a == 0) and (b == 0)):
	    ret_values.append('NO')
	elif (abs((a - b)) <= 1):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
