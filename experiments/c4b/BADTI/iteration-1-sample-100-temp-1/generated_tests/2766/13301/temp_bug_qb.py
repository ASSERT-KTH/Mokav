def original_func(*args):
	global_list = []
	
	s = args[0]
	global_list.append(('YES' if (sum(((s[i] != s[((- i) - 1)]) for i in range((len(s) // 2)))) <= 1) else 'NO'))
	return global_list