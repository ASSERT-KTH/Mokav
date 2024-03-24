def func(*args):
	ret_values = []
	
	x = args[0]
	m = len(''.join(set(x)))
	m = int(m)
	if ((m % 2) == 0):
	    ret_values.append('CHAT WITH HER!')
	else:
	    ret_values.append('IGNORE HIM!')

	return ret_values
