def patched_func(*args):
	global_list = []
	
	lisa = args[0]
	if (('H' in lisa) or ('Q' in lisa) or ('9' in lisa)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list