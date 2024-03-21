def func(*args):
	ret_values = []
	
	ret_values.append('YNEOS'[(not (set('HQ9') & set(args[0])))::2])

	return ret_values
