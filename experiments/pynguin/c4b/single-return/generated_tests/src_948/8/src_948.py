def func(*args):
	
	return(['NO', 'YES'][(sum(((x in ['H', 'Q', '9']) for x in args[0])) > 0)])
