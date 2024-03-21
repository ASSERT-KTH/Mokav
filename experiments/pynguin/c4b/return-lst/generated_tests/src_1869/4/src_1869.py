def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n & 1):
	    ret_values.append((n // 2))
	else:
	    k = 1
	    while (k <= n):
	        k *= 2
	    ret_values.append(((n - (k // 2)) // 2))

	return ret_values
