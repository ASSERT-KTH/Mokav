def func(*args):
	ret_values = []
	
	(l, b) = map(int, args[0].split())
	i = 0
	while (b >= l):
	    l *= 3
	    b *= 2
	    i += 1
	ret_values.append(i)

	return ret_values
