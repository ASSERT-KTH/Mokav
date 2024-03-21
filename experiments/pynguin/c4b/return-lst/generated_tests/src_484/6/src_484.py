def func(*args):
	ret_values = []
	
	a = '6842'
	n = int(args[0])
	if (n == 0):
	    ret_values.append(1)
	else:
	    n %= 4
	    ret_values.append(a[n])

	return ret_values
