def func(*args):
	ret_values = []
	
	a = args[0]
	a = list(a)
	H = 'NO'
	for x in a:
	    if ((x == 'H') or (x == 'Q') or (x == '9')):
	        H = 'YES'
	ret_values.append(H)

	return ret_values
