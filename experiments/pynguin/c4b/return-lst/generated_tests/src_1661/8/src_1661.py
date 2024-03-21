def func(*args):
	ret_values = []
	
	(a, b, c, d) = sorted(map(int, args[0].split()))
	if ((d < (c + b)) or (c < (b + a))):
	    ret_values.append('TRIANGLE')
	elif ((d == (c + b)) or (c == (b + a))):
	    ret_values.append('SEGMENT')
	else:
	    ret_values.append('IMPOSSIBLE')

	return ret_values
