def func(*args):
	ret_values = []
	
	ret_values.append(['NO', 'YES'][bool((set('HQ9') & set(args[0])))])

	return ret_values
