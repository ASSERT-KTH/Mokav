def func(*args):
	ret_values = []
	
	n = args[0]
	n = int(n)
	if (n == 0):
	    ret_values.append(1)
	else:
	    a = [6, 8, 4, 2]
	    n = (n % 4)
	    ret_values.append(a[n])

	return ret_values
