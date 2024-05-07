def original_func(*args):
	global_list = []
	
	a = args[0]
	b = args[1]
	c = args[2]
	d = ((a + b) + c)
	if ('X' in d):
	    if (d == d[::(- 1)]):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	else:
	    global_list.append('NO')
	return global_list