def func(*args):
	ret_values = []
	
	x = int(args[0])
	for i in range(x):
	    if ((i % 2) == 0):
	        ret_values.append('I hate', end=' ')
	    elif ((i % 2) == 1):
	        ret_values.append('I love', end=' ')
	    if (i == (x - 1)):
	        ret_values.append('it')
	    else:
	        ret_values.append('that', end=' ')

	return ret_values
