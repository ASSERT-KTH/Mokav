def func(*args):
	ret_values = []
	
	n = int(args[0])
	for i in range(n):
	    if (i % 2):
	        ret_values.append('I love', end=' ')
	    else:
	        ret_values.append('I hate', end=' ')
	    if ((i + 1) < n):
	        ret_values.append('that', end=' ')
	    else:
	        ret_values.append('it')

	return ret_values
