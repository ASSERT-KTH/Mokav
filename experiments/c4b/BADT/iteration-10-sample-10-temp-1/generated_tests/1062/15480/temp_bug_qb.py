def original_func(*args):
	global_list = []
	
	n = sum([1 for i in args[0] if (i in (4, 7))])
	global_list.append(('YES' if set(str(n)).issubset(set('47')) else 'NO'))
	return global_list