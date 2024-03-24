def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split(' '))
	if (a == b == 0):
	    ret_values.append('NO')
	elif ((abs((a - b)) == 1) or (a == b)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
