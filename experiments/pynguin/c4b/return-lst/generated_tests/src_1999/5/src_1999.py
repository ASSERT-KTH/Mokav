def func(*args):
	ret_values = []
	
	str_input = str(args[0])
	if ((len(''.join(set(str_input))) % 2) == 0):
	    ret_values.append('CHAT WITH HER!')
	else:
	    ret_values.append('IGNORE HIM!')

	return ret_values
