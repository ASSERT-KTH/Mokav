def original_func(*args):
	global_list = []
	
	a = args[0]
	if (1 <= len(a) <= 100):
	    if ('H' in a):
	        global_list.append('YES')
	    if ('Q' in a):
	        global_list.append('YES')
	    if ('(' in a):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	else:
	    global_list.append('too long string')
	return global_list