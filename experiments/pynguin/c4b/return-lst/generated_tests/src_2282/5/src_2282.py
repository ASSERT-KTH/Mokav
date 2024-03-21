def func(*args):
	ret_values = []
	
	s = str(args[0])
	s = set(s)
	if ((len(s) % 2) == 0):
	    ret_values.append('CHAT WITH HER!')
	else:
	    ret_values.append('IGNORE HIM!')

	return ret_values
