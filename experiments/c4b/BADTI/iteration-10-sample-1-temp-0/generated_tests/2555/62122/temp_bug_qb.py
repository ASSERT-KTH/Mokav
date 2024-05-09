def original_func(*args):
	global_list = []
	
	a = args[0]
	if (('1111111' not in a) and ('0000000' not in a)):
	    global_list.append('NO')
	global_list.append('YES')
	return global_list