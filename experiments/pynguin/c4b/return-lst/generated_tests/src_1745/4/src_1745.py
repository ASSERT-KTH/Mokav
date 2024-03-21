def func(*args):
	ret_values = []
	
	(h1, h2) = map(int, args[0].split())
	diffe = (h2 - h1)
	(a, b) = map(int, args[1].split())
	if ((h1 + (a * 8)) >= h2):
	    ret_values.append(0)
	elif (a > b):
	    num = ((h2 - h1) - (8 * a))
	    den = (12 * (a - b))
	    ret_values.append(int((((num + den) - 1) / den)))
	else:
	    ret_values.append((- 1))

	return ret_values
