def func(*args):
	ret_values = []
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	while (((a * 4) > c) or ((a * 2) > b)):
	    a = (a - 1)
	ret_values.append(((a + (a * 2)) + (a * 4)))

	return ret_values
