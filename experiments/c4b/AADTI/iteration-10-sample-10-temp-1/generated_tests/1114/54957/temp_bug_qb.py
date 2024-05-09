def original_func(*args):
	global_list = []
	
	a = args[0]
	b = args[1]
	c = args[2]
	if (a[0] == c[2]):
	    d = 0
	else:
	    d = 1
	if (a[1] == c[1]):
	    d = 0
	else:
	    d = 1
	if (a[2] == c[0]):
	    d = 0
	else:
	    d = 1
	if (b[0] == b[2]):
	    d = 0
	else:
	    d = 1
	if (d == 0):
	    global_list.append('YES')
	if (d == 1):
	    global_list.append('NO')
	return global_list