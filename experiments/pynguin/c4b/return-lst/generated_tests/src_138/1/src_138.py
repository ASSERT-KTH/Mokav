def func(*args):
	ret_values = []
	
	'input\n0 60 50\n'
	(a, b, c) = map(int, args[0].split())
	if (a == b):
	    ret_values.append('YES')
	elif (c == 0):
	    ret_values.append('NO')
	elif ((((b - a) % c) == 0) and (b > a) and (c > 0)):
	    ret_values.append('YES')
	elif ((((b - a) % c) == 0) and (a > b) and (c < 0)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
