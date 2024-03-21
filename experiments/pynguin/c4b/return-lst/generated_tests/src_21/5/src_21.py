def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	if ((m % 2) == 1):
	    ret_values.append(((n * (m // 2)) + (n // 2)))
	else:
	    ret_values.append((n * (m // 2)))

	return ret_values
