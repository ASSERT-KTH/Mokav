def patched_func(*args):
	global_list = []
	
	global_list.append(('CHAT WITH HER!', 'IGNORE HIM!')[(len(set(args[0])) % 2)])
	return global_list