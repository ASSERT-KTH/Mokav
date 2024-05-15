def patched_func(*args):
	global_list = []
	
	import sys
	m = int(args[0])
	if ((((m - 2) % 2) == 0) and (m > 2)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list