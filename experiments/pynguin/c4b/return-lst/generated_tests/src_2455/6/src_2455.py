def func(*args):
	ret_values = []
	
	nombre = args[0]
	set = set(nombre)
	if ((len(set) % 2) == 0):
	    ret_values.append('CHAT WITH HER!')
	else:
	    ret_values.append('IGNORE HIM!')

	return ret_values
