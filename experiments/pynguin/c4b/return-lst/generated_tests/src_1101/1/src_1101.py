def func(*args):
	ret_values = []
	
	n = int(args[0])
	ret_values.append('I hate', end=' ')
	for i in range(1, (n + 1)):
	    if (i == n):
	        ret_values.append('it')
	    elif ((i % 2) == 0):
	        ret_values.append('that I hate', end=' ')
	    else:
	        ret_values.append('that I love', end=' ')

	return ret_values
