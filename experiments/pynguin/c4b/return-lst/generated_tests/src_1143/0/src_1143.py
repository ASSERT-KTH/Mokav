def func(*args):
	ret_values = []
	
	(n, a, b) = args[0].split()
	(n, a, b) = (int(n), int(a), int(b))
	if ((a + b) >= n):
	    if ((n - a) >= 0):
	        ret_values.append((n - a))
	    else:
	        ret_values.append(0)
	else:
	    ret_values.append((b + 1))

	return ret_values
