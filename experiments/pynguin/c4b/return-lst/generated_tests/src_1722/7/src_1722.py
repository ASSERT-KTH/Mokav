def func(*args):
	ret_values = []
	
	str = args[0]
	n_lower = 0
	n_upper = 0
	for c in str:
	    if c.islower():
	        n_lower += 1
	    elif c.isupper():
	        n_upper += 1
	if (n_upper > n_lower):
	    ret_values.append(str.upper())
	else:
	    ret_values.append(str.lower())

	return ret_values
