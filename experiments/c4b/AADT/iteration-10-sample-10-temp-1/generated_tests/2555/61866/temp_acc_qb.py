def patched_func(*args):
	global_list = []
	
	a = args[0]
	global_list.append(['NO', 'YES'][((('0' * 7) in a) or (('1' * 7) in a))])
	return global_list