def func(*args):
	ret_values = []
	
	s = args[0]
	ret_values.append(['NO', 'YES'][(('H' in s) or ('Q' in s) or ('9' in s))])

	return ret_values
