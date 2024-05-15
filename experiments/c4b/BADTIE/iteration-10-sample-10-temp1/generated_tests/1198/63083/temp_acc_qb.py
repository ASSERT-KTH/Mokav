def patched_func(*args):
	global_list = []
	
	line = args[0]
	if (('H' in line) or ('Q' in line) or ('9' in line)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list