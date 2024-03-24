def func(*args):
	ret_values = []
	
	ret_values.append(['NO', 'YES'][(sum(((x in ['H', 'Q', '9']) for x in args[0])) > 0)])

	return ret_values
