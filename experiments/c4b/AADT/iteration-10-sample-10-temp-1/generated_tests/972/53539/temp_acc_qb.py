def patched_func(*args):
	global_list = []
	
	(a, b) = args[0].split()
	a = int(a)
	b = int(b)
	if ((abs((a - b)) > 1) or ((not a) and (not b))):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list