def patched_func(*args):
	global_list = []
	
	code = args[0]
	if (('H' in code) or ('Q' in code) or ('9' in code)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list