def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	i = 0
	while (a <= b):
	    a *= 3
	    b *= 2
	    i += 1
	ret_values.append(i)

	return ret_values
