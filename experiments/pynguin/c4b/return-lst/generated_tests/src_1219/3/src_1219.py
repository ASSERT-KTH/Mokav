def func(*args):
	ret_values = []
	
	a = int(args[0])
	ret_values.append(a, end=' ')
	if (a > 1):
	    ret_values.append(' '.join(map(str, range(1, a))))

	return ret_values
