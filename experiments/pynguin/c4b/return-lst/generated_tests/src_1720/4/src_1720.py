def func(*args):
	ret_values = []
	
	n = int(args[0])
	x = []
	if ((n % 2) != 0):
	    ret_values.append((- 1))
	else:
	    for i in range(int((n / 2))):
	        ret_values.append(((i * 2) + 2), end=' ')
	        ret_values.append(((i * 2) + 1), end=' ')
	    ret_values.append('')

	return ret_values
