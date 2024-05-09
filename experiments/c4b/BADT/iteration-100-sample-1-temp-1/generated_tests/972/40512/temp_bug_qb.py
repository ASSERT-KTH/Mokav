def original_func(*args):
	global_list = []
	
	(x, y) = args[0].split()
	x = int(x)
	y = int(y)
	if (((x - y) > 1) or ((x - y) < (- 1))):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list