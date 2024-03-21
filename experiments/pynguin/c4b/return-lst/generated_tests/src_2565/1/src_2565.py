def func(*args):
	ret_values = []
	
	sides = [int(i) for i in args[0].split()]
	(a, b, c, d) = sides
	if (((a + b) > c) and ((a + c) > b) and ((c + b) > a)):
	    ret_values.append('TRIANGLE')
	elif (((a + c) > d) and ((a + d) > c) and ((c + d) > a)):
	    ret_values.append('TRIANGLE')
	elif (((b + c) > d) and ((b + d) > c) and ((c + d) > b)):
	    ret_values.append('TRIANGLE')
	elif (((a + d) > b) and ((a + b) > d) and ((b + d) > a)):
	    ret_values.append('TRIANGLE')
	elif (((a + b) == c) or ((a + c) == b) or ((c + b) == a)):
	    ret_values.append('SEGMENT')
	elif (((a + c) == d) or ((a + d) == c) or ((c + d) == a)):
	    ret_values.append('SEGMENT')
	elif (((b + c) == d) or ((b + d) == c) or ((c + d) == b)):
	    ret_values.append('SEGMENT')
	elif (((a + d) == b) or ((a + b) == d) or ((b + d) == a)):
	    ret_values.append('SEGMENT')
	else:
	    ret_values.append('IMPOSSIBLE')

	return ret_values
