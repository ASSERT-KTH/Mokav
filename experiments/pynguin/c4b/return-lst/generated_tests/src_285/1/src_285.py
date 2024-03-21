def func(*args):
	ret_values = []
	
	n = int(args[0])
	ret_values.append('I hate', end=' ')
	for i in range(2, (n + 1)):
	    if ((i % 2) == 0):
	        ret_values.append('that I love', end=' ')
	    elif ((i % 2) != 0):
	        ret_values.append('that I hate', end=' ')
	ret_values.append('it')

	return ret_values
