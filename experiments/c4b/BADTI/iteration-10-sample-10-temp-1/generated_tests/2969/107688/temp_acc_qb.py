def patched_func(*args):
	global_list = []
	
	(s, v1, v2, t1, t2) = [int(i) for i in args[0].split()]
	if (((s * v1) + (2 * t1)) < ((s * v2) + (2 * t2))):
	    global_list.append('First')
	elif (((s * v1) + (2 * t1)) > ((s * v2) + (2 * t2))):
	    global_list.append('Second')
	else:
	    global_list.append('Friendship')
	return global_list