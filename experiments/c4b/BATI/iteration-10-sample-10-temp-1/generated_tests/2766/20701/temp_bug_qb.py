def original_func(*args):
	global_list = []
	
	s = args[0]
	global_list.append(['YES', 'NO'][(len([s[i] for i in range((len(s) // 2)) if (s[i] != s[((len(s) - i) - 1)])]) != 1)])
	return global_list