def patched_func(*args):
	global_list = []
	
	(even, odd) = (int(x) for x in args[0].split())
	if (abs((even - odd)) > 1):
	    global_list.append('NO')
	elif ((even == 0) and (odd == 0)):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list