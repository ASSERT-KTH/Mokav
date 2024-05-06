def patched_func(*args):
	global_list = []
	
	x = args[0]
	i = 0
	j = 1
	if ((x.find('9') != (- 1)) or (x.find('H') != (- 1)) or (x.find('Q') != (- 1))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list