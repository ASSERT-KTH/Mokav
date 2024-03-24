def func(*args):
	ret_values = []
	
	(n, a, b) = map(int, args[0].split())
	if ((((a + b) % n) % n) == 0):
	    ret_values.append(n)
	else:
	    ret_values.append((((a + b) % n) % n))

	return ret_values
