def original_func(*args):
	global_list = []
	
	from collections import Counter
	global_list.append(('CHAT WITH HER' if ((len(Counter(args[0]).keys()) % 2) == 0) else 'IGNORE HIM'))
	return global_list