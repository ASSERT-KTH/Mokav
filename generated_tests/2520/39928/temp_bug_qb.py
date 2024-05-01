def original_func(*args):
	global_list = []
	
	(y, w) = [int(x) for x in args[0].split(' ')]
	m = max(y, w)
	denominator = 6
	numerator = ((denominator - m) + 1)
	if (((numerator % 2) == 0) and ((denominator % 2) == 0)):
	    numerator /= 2
	    denominator /= 2
	elif (((numerator % 3) == 0) and ((denominator % 3) == 0)):
	    numerator /= 3
	    denominator /= 3
	global_list.append(((str(int(numerator)) + '/') + str(int(denominator))))
	return global_list