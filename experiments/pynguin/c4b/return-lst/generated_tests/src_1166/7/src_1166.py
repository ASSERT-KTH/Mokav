def func(*args):
	ret_values = []
	
	i = (int(args[0]) + 1)
	while (len(set(str(i))) != 4):
	    i += 1
	ret_values.append(i)

	return ret_values
