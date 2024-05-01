def original_func(*args):
	global_list = []
	
	p = args[0]
	if (('H' in p) or ('Q' in p) or ('9' in p) or ('+' in p)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list