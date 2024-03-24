def func(*args):
	ret_values = []
	
	n = int(args[0])
	i = 0
	while ((5 * (2 ** i)) < n):
	    n = (n - (5 * (2 ** i)))
	    i += 1
	if ((n / (5 * (2 ** i))) <= 0.2):
	    ret_values.append('Sheldon')
	elif ((n / (5 * (2 ** i))) <= 0.4):
	    ret_values.append('Leonard')
	elif ((n / (5 * (2 ** i))) <= 0.6):
	    ret_values.append('Penny')
	elif ((n / (5 * (2 ** i))) <= 0.8):
	    ret_values.append('Rajesh')
	else:
	    ret_values.append('Howard')

	return ret_values
