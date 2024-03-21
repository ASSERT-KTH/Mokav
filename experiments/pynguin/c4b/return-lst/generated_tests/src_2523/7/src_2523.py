def func(*args):
	ret_values = []
	
	stri = args[0]
	b = []
	b = list(set(stri))
	if ((len(b) % 2) == 0):
	    ret_values.append('CHAT WITH HER!')
	else:
	    ret_values.append('IGNORE HIM!')

	return ret_values
