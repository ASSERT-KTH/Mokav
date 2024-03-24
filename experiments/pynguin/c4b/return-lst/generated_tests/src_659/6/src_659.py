def func(*args):
	ret_values = []
	
	(l, r) = [int(x) for x in args[0].split()]
	if (l == r):
	    ret_values.append(l)
	else:
	    ret_values.append(2)

	return ret_values
