def func(*args):
	ret_values = []
	
	'input\n0 1\n'
	(a, b) = map(int, args[0].split())
	if ((a == 0) and (b == 0)):
	    ret_values.append('NO')
	elif (abs((a - b)) <= 1):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
