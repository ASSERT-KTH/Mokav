def func(*args):
	
	a = args[0]
	return(['NO', 'YES'][((('0' * 7) in a) or (('1' * 7) in a))])
