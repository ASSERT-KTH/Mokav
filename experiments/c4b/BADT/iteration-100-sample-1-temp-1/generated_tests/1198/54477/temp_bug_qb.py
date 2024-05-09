def original_func(*args):
	global_list = []
	
	s = args[0]
	result = ''
	for x in s:
	    if (x in 'HQ9+'):
	        global_list.append('YES')
	    else:
	        result += x
	global_list.append('NO')
	return global_list