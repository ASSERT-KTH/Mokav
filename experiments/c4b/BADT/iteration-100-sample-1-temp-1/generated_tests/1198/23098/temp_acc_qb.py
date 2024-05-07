def patched_func(*args):
	global_list = []
	
	n = args[0]
	if (('H' in n) or ('Q' in n) or ('9' in n)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list