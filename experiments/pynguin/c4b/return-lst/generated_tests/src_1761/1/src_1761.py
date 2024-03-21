def func(*args):
	ret_values = []
	
	x = int(args[0])
	c = 0
	while (x > 0):
	    d = (x % 8)
	    c += (d == 1)
	    x = (x // 8)
	ret_values.append(c)

	return ret_values
