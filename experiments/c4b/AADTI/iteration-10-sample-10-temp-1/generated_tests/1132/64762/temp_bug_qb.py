def original_func(*args):
	global_list = []
	
	''.join((e for e in [('.' + letter) for letter in list(args[0].lower()) if (letter not in ['a', 'o', 'y', 'e', 'u', 'i'])]))
	return global_list