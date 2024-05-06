def original_func(*args):
	global_list = []
	
	program = args[0]
	if (('H' in program) or ('Q' is program) or ('9' in program) or ('+' in program)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list