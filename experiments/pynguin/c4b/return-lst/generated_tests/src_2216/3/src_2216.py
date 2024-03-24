def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	x = 0
	while (a <= b):
	    x += 1
	    a *= 3
	    b *= 2
	ret_values.append(x)

	return ret_values
