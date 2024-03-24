def func(*args):
	ret_values = []
	
	a = args[0]
	b = a.split()
	if (int(b[0]) == int(b[1])):
	    ret_values.append(int(b[0]))
	else:
	    ret_values.append(2)

	return ret_values
