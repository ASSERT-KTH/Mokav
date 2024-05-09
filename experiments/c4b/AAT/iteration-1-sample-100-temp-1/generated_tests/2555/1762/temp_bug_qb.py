def original_func(*args):
	global_list = []
	
	a = args[0]
	global_list.append(['YES', 'NO'][all(((len(set(a[(i - 7):i])) > 1) for i in range(7, len(a))))])
	return global_list