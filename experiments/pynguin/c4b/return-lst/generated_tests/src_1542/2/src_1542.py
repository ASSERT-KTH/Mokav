def func(*args):
	ret_values = []
	
	name = args[0]
	chars = set(name)
	if ((len(chars) % 2) == 0):
	    ret_values.append('CHAT WITH HER!')
	else:
	    ret_values.append('IGNORE HIM!')

	return ret_values
