def patched_func(*args):
	global_list = []
	
	(s, v1, v2, t1, t2) = map(int, args[0].split())
	if (((s * v1) + (t1 * 2)) < ((s * v2) + (t2 * 2))):
	    global_list.append('First')
	elif (((s * v1) + (t1 * 2)) > ((s * v2) + (t2 * 2))):
	    global_list.append('Second')
	else:
	    global_list.append('Friendship')
	return global_list