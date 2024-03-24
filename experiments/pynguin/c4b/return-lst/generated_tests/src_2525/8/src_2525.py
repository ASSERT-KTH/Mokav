def func(*args):
	ret_values = []
	
	ret_values.append(('CHAT WITH HER!', 'IGNORE HIM!')[(len(set(args[0])) % 2)])

	return ret_values
