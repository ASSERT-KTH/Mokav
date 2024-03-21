def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	if ((a == 0) and (b == 0)):
	    ret_values.append('NO')
	elif (abs((a - b)) > 1):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
