def func(*args):
	ret_values = []
	
	a = args[0]
	l = len(a)
	if (l != 1):
	    b = (10 ** (l - 1))
	    ret_values.append((b - int(a[1:])))
	else:
	    ret_values.append(1)

	return ret_values
