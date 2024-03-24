def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n % 2) == 0):
	    for i in range(0, (n // 2)):
	        ret_values.append(1, end='')
	else:
	    ret_values.append(7, end='')
	    for i in range(0, ((n // 2) - 1)):
	        ret_values.append(1, end='')

	return ret_values
