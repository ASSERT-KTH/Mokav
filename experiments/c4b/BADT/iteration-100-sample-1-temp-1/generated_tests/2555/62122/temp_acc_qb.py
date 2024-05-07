def patched_func(*args):
	global_list = []
	
	a = args[0]
	if (('1111111' in a) or ('0000000' in a)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list