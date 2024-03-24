def func(*args):
	
	s = args[0]
	return(['NO', 'YES'][(('H' in s) or ('Q' in s) or ('9' in s))])
