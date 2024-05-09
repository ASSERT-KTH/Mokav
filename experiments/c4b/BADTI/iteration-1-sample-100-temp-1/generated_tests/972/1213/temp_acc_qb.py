def patched_func(*args):
	global_list = []
	
	(a, b) = args[0].split()
	(a, b) = (int(a), int(b))
	if ((abs((a - b)) > 1) or ((a == 0) and (b == 0))):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list