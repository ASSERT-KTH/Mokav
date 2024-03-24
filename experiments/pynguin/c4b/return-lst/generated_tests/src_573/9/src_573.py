def func(*args):
	ret_values = []
	
	(n, k, l, c, d, p, nl, np) = map(int, args[0].split())
	x = int((((k * l) - ((k * l) % nl)) / nl))
	y = (c * d)
	z = int((p / np))
	if (x > y):
	    if (y > z):
	        ret_values.append(int((z / n)))
	    else:
	        ret_values.append(int((y / n)))
	elif (x > z):
	    ret_values.append(int((z / n)))
	else:
	    ret_values.append(int((x / n)))

	return ret_values
