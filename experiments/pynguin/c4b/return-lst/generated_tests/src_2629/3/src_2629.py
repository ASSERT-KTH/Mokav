def func(*args):
	ret_values = []
	
	n = int(args[0])
	k = (int((n / 2)) - 1)
	if ((n - (k * 2)) == 3):
	    ret_values.append(7, end='')
	else:
	    ret_values.append(1, end='')
	for i in range(k):
	    ret_values.append(1, end='')

	return ret_values
