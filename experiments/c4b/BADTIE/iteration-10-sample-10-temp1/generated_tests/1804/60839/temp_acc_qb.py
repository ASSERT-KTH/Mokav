def patched_func(*args):
	global_list = []
	
	global_list.append(('IGNORE HIM!' if (len(set(args[0])) % 2) else 'CHAT WITH HER!'))
	return global_list