def patched_func(*args):
	global_list = []
	
	(s, v1, v2, t1, t2) = map(int, args[0].split())
	first = ((t1 + (v1 * s)) + t1)
	second = ((t2 + (v2 * s)) + t2)
	if (first < second):
	    global_list.append('First')
	elif (first > second):
	    global_list.append('Second')
	else:
	    global_list.append('Friendship')
	return global_list