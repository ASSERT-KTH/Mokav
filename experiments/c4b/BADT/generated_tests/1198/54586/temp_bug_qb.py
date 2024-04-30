def original_func(*args):
	global_list = []
	
	a = args[0]
	if (('H' in a) or ('Q' in a) or ('+' in a) or ('9' in a)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list