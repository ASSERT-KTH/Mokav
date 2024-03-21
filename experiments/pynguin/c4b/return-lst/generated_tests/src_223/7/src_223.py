def func(*args):
	ret_values = []
	
	ret_values.append(['YES', 'NO'][(not (set('HQ9') & set(args[0])))])

	return ret_values
