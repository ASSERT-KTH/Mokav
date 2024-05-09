def original_func(*args):
	global_list = []
	
	a = args[0]
	b = 'HQ9+'
	j = 0
	for i in a:
	    if (i in b):
	        break
	    j += 1
	if (len(a) == j):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list