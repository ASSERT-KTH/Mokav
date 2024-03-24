def func(*args):
	ret_values = []
	
	name = set(list(args[0]))
	if ((len(name) % 2) == 0):
	    ret_values.append('CHAT WITH HER!')
	else:
	    ret_values.append('IGNORE HIM!')

	return ret_values
