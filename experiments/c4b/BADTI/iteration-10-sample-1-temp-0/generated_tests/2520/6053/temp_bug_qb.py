def original_func(*args):
	global_list = []
	
	(y, w) = [int(x) for x in args[0].split()]
	numerator = ((6 - max(y, w)) + 1)
	if (numerator == 0):
	    prob = '0/1'
	elif (numerator == 1):
	    prob = '1/1'
	elif (numerator == 2):
	    prob = '1/3'
	elif (numerator == 3):
	    prob = '1/2'
	elif (numerator == 4):
	    prob = '2/3'
	elif (numerator == 5):
	    prob = '5/6'
	elif (numerator == 6):
	    prob = '1/1'
	global_list.append(prob)
	return global_list