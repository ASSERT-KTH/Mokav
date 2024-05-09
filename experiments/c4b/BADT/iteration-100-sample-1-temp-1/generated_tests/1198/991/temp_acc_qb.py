def patched_func(*args):
	global_list = []
	
	global_list.append(['YES', 'NO'][(not (set('HQ9') & set(args[0])))])
	return global_list