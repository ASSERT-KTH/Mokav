def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].strip().split())
	c = 0
	while (a <= b):
	    a *= 3
	    b *= 2
	    c += 1
	ret_values.append(c)

	return ret_values
