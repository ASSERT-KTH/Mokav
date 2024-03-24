def func(*args):
	ret_values = []
	
	a = int(args[0])
	for i in range((a - 1)):
	    if ((i % 2) == 0):
	        ret_values.append('I hate that', end=' ')
	    else:
	        ret_values.append('I love that', end=' ')
	if ((a % 2) == 0):
	    ret_values.append('I love it')
	else:
	    ret_values.append('I hate it')

	return ret_values
