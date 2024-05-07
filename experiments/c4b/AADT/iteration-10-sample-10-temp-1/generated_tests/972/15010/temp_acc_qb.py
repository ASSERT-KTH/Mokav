def patched_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].strip().split())
	if ((abs((a - b)) < 2) and ((a + b) != 0)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list