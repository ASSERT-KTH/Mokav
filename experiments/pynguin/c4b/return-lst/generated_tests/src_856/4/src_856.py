def func(*args):
	ret_values = []
	
	a = str(args[0])
	b = set(a)
	length = len(b)
	if ((length % 2) == 0):
	    ret_values.append('CHAT WITH HER!')
	else:
	    ret_values.append('IGNORE HIM!')

	return ret_values
