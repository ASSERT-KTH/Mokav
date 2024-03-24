def func(*args):
	ret_values = []
	
	a = args[0]
	ret_values.append(['NO', 'YES'][((('0' * 7) in a) or (('1' * 7) in a))])

	return ret_values
