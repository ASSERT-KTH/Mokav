def patched_func(*args):
	global_list = []
	
	s = list(args[0])
	i = ['H', 'Q', '9']
	if any([x for x in i if (x in s)]):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list