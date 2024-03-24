def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n % 2) == 1):
	    ret_values.append((- 1))
	else:
	    a = list(range(1, (n + 1)))
	    for i in range(0, n, 2):
	        (a[i], a[(i + 1)]) = (a[(i + 1)], a[i])
	    ret_values.append(*a)

	return ret_values
