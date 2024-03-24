def func(*args):
	ret_values = []
	
	(k, r) = map(int, args[0].split())
	i = 1
	while (((((i * k) - r) % 10) != 0) and (((i * k) % 10) != 0)):
	    i += 1
	ret_values.append(i)

	return ret_values
