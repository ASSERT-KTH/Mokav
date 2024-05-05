def patched_func(*args):
	global_list = []
	
	text = args[0]
	if (('H' in text) or ('Q' in text) or ('9' in text)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list