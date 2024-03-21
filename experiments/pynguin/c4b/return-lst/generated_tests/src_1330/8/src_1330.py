def func(*args):
	ret_values = []
	
	(a, b, c) = args[0].strip().split(' ')
	(a, b, c) = (int(a), int(b), int(c))
	m = max(a, b, c)
	if ((a == b) and (b == c)):
	    ret_values.append(0)
	    exit()
	if ((a == m) and (b < a) and (c < a)):
	    ret_values.append(((((2 * a) - 2) - b) - c))
	elif ((b == m) and (b > c)):
	    if (a < b):
	        ret_values.append((((((b - 1) + b) - 1) - a) - c))
	    elif (a == b):
	        ret_values.append(((((2 * b) - 1) - a) - c))
	elif (m == c):
	    if ((a < c) and (b < c)):
	        ret_values.append(((((c + c) - 2) - a) - b))
	    elif ((a == c) and (b < c)):
	        ret_values.append(((c - 1) - b))
	    elif ((a < c) and (b == c)):
	        ret_values.append(((c - 1) - a))

	return ret_values
