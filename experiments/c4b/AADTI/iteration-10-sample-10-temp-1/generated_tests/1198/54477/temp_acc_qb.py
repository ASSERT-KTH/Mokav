def patched_func(*args):
	global_list = []
	
	s = args[0]
	global_list.append(['NO', 'YES'][(('H' in s) or ('Q' in s) or ('9' in s))])
	return global_list