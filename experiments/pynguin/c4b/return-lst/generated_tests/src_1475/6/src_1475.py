def func(*args):
	ret_values = []
	
	n = args[0]
	if ((len(set(n)) % 2) == 0):
	    ret_values.append('CHAT WITH HER!')
	else:
	    ret_values.append('IGNORE HIM!')

	return ret_values
