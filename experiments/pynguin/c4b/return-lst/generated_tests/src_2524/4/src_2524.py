def func(*args):
	ret_values = []
	
	if ((len(set(args[0])) % 2) == 0):
	    ret_values.append('CHAT WITH HER!')
	else:
	    ret_values.append('IGNORE HIM!')

	return ret_values
