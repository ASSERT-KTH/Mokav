def func(*args):
	ret_values = []
	
	n = int(args[0])
	ret_values.append(n, end=' ')
	for i in range(1, n):
	    ret_values.append(i, end=' ')

	return ret_values
