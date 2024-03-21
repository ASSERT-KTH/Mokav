def func(*args):
	ret_values = []
	
	(a, b, c) = map(int, args[0].split())
	g = ((c - ((b / a) * 100)) / (100 / a))
	if ((g > 0) and (int(g) != g)):
	    g = (int(g) + 1)
	(ret_values.append(int(g)) if (g > 0) else ret_values.append(0))

	return ret_values
