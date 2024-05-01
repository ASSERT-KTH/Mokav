def patched_func(*args):
	global_list = []
	
	global_list.append(('YES' if any(((c in 'HQ9') for c in args[0])) else 'NO'))
	return global_list