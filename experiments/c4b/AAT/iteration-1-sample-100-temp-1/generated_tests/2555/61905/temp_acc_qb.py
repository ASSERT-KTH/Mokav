def patched_func(*args):
	global_list = []
	
	n = args[0]
	if (('1111111' in n) or ('0000000' in n)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list