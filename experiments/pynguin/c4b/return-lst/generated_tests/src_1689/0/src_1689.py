def func(*args):
	ret_values = []
	
	
	def tri(a, b, c, d):
	    if ((((a + b) > c) and ((a + c) > b) and ((b + c) > a)) or (((d + b) > c) and ((d + c) > b) and ((b + c) > d)) or (((a + d) > c) and ((a + c) > d) and ((d + c) > a)) or (((a + b) > d) and ((a + d) > b) and ((b + d) > a))):
	        ret_values.append('TRIANGLE')
	    elif (((a + b) == c) or ((a + c) == b) or ((b + c) == a) or ((d + b) == c) or ((d + c) == b) or ((b + c) == d) or ((a + d) == c) or ((a + c) == d) or ((d + c) == a) or ((a + b) == d) or ((b + d) == a) or ((a + d) == b)):
	        ret_values.append('SEGMENT')
	    else:
	        ret_values.append('IMPOSSIBLE')
	(a, b, c, d) = map(int, args[0].split(' '))
	tri(a, b, c, d)

	return ret_values
