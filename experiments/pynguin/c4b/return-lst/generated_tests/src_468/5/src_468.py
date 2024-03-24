def func(*args):
	ret_values = []
	
	(a, b, c) = map(int, args[0].split(' '))
	if (a == b):
	    ret_values.append('YES')
	elif ((a != b) and (c == 0)):
	    ret_values.append('NO')
	elif ((((b - a) % c) == 0) and (((b - a) / c) > 0)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
