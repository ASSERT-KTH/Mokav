def func(*args):
	ret_values = []
	
	(a, b, c, d) = map(int, args[0].split())
	if (((a + b) > c) and ((a + c) > b) and ((b + c) > a)):
	    ret_values.append('TRIANGLE')
	elif (((a + b) > d) and ((a + d) > b) and ((b + d) > a)):
	    ret_values.append('TRIANGLE')
	elif (((a + c) > d) and ((a + d) > c) and ((c + d) > a)):
	    ret_values.append('TRIANGLE')
	elif (((b + c) > d) and ((b + d) > c) and ((c + d) > b)):
	    ret_values.append('TRIANGLE')
	elif (((a + b) == c) or ((a + c) == b) or ((b + c) == a)):
	    ret_values.append('SEGMENT')
	elif (((a + b) == d) or ((a + d) == b) or ((b + d) == a)):
	    ret_values.append('SEGMENT')
	elif (((a + c) == d) or ((a + d) == c) or ((c + d) == a)):
	    ret_values.append('SEGMENT')
	elif (((b + c) == d) or ((b + d) == c) or ((c + d) == b)):
	    ret_values.append('SEGMENT')
	else:
	    ret_values.append('IMPOSSIBLE')

	return ret_values
