def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n <= 2):
	    ret_values.append((- 1))
	else:
	    numbers = [x for x in range(n, 0, (- 1))]
	    ret_values.append(' '.join(map(str, numbers)))

	return ret_values
