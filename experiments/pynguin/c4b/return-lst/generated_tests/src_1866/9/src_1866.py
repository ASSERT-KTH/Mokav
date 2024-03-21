def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n % 2) == 1):
	    ret_values.append(7, end='')
	    n -= 3
	while (n > 1):
	    ret_values.append(1, end='')
	    n -= 2

	return ret_values
