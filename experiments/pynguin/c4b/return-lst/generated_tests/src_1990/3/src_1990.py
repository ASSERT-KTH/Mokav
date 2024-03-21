def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n & 1):
	    ret_values.append(7, end='')
	    for i in range(((n - 3) // 2)):
	        ret_values.append(1, end='')
	else:
	    for i in range((n // 2)):
	        ret_values.append(1, end='')
	ret_values.append('')

	return ret_values
