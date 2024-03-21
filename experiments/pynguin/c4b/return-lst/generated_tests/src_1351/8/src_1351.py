def func(*args):
	ret_values = []
	
	x = args[0]
	(capital, small, i) = (0, 0, 0)
	while (i < len(x)):
	    if (x[i].isupper() == True):
	        capital += 1
	    else:
	        small += 1
	    i += 1
	if (small >= capital):
	    ret_values.append(x.lower())
	else:
	    ret_values.append(x.upper())

	return ret_values
