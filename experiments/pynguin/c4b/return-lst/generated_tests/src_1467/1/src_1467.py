def func(*args):
	ret_values = []
	
	a = args[0]
	(l, r) = a.split(' ')
	if (int(l) == int(r)):
	    ret_values.append(l)
	else:
	    ret_values.append('2')

	return ret_values
