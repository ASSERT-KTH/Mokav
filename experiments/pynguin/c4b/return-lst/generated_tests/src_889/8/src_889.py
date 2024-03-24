def func(*args):
	ret_values = []
	
	(y, w) = [int(x) for x in args[0].split()]
	numerator = ((6 - max(y, w)) + 1)
	if (numerator == 0):
	    prob = '0/1'
	elif (numerator == 1):
	    prob = '1/6'
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
	ret_values.append(prob)

	return ret_values
