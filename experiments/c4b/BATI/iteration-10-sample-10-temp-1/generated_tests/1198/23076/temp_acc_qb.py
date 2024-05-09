def patched_func(*args):
	global_list = []
	
	string = args[0]
	if (('H' in string) or ('Q' in string) or ('9' in string)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list