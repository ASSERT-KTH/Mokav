def original_func(*args):
	global_list = []
	
	l = list(args[0])
	if ('H' in l):
	    global_list.append('YES')
	elif ('Q' in l):
	    global_list.append('TES')
	elif ('9' in l):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list