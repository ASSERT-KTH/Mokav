def func(*args):
	ret_values = []
	
	(a, b, c, d) = sorted((int(x) for x in args[0].split()))
	if (((a + b) > c) or ((b + c) > d)):
	    ret_values.append('TRIANGLE')
	elif (((a + b) == c) or ((a + b) == d) or ((b + c) == d)):
	    ret_values.append('SEGMENT')
	else:
	    ret_values.append('IMPOSSIBLE')

	return ret_values
