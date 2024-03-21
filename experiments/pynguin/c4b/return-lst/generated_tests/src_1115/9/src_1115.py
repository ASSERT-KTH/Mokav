def func(*args):
	ret_values = []
	
	(n, a) = map(int, args[0].split())
	if ((a % 2) == 1):
	    ret_values.append(int(((a + 1) / 2)))
	else:
	    ret_values.append(int((((n - a) / 2) + 1)))

	return ret_values
