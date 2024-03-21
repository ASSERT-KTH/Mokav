def func(*args):
	ret_values = []
	
	(a, b) = [int(i) for i in args[0].split()]
	if (a == b):
	    ret_values.append(a)
	else:
	    ret_values.append(2)

	return ret_values
