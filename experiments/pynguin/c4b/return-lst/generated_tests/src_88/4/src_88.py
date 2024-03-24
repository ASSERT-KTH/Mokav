def func(*args):
	ret_values = []
	
	(a, b, c) = map(int, args[0].split())
	k = (((a < b) * (c > 0)) + ((a > b) * (c < 0)))
	if (a == b):
	    ret_values.append('YES')
	elif (c == 0):
	    ret_values.append('NO')
	elif (((c == 0) and (a == b)) or (k and (((b - a) % c) == 0))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
