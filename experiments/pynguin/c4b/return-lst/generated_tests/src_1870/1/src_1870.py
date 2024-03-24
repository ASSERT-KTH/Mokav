def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n % 2) == 1):
	    ret_values.append((n // 2))
	else:
	    x = 1
	    while (x <= n):
	        x *= 2
	    ret_values.append(((n - (x // 2)) // 2))

	return ret_values
