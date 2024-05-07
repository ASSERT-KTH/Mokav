def patched_func(*args):
	global_list = []
	
	x = args[0]
	y = (x.count('4') + x.count('7'))
	if ((y == 4) or (y == 7)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list