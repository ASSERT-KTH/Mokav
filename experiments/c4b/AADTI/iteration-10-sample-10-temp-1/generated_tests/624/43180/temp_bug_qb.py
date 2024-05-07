def original_func(*args):
	global_list = []
	
	(a, b, c) = args[0].split()
	(prvni, interval, jist) = [int(a), int(b), int(c)]
	if ((jist >= prvni) and (jist != (prvni + 1)) and (((jist % interval) == prvni) or ((jist % interval) == (prvni + 1)))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list