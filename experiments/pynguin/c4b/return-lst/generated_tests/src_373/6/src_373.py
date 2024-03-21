def func(*args):
	ret_values = []
	
	a = args[0]
	b = a.split()
	if (((int(b[0]) % 2) == 1) and ((int(b[1]) % 2) == 1)):
	    ret_values.append(int((((int(b[0]) * int(b[1])) - 1) / 2)))
	else:
	    ret_values.append(int(((int(b[0]) * int(b[1])) / 2)))

	return ret_values
