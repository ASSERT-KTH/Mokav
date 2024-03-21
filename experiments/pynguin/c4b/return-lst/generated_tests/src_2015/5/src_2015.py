def func(*args):
	ret_values = []
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	i = (a * 2)
	z = (a * 4)
	while ((i > b) or (z > c)):
	    a -= 1
	    i = (a * 2)
	    z = (a * 4)
	ret_values.append((a * 7))

	return ret_values
