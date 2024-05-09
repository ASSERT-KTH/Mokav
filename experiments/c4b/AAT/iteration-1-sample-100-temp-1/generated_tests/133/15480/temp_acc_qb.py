def patched_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split())
	(x, y, z) = map(int, args[1].split())
	need = ((max((x - a), 0) + max((y - b), 0)) + max((z - c), 0))
	extra = ((((max((a - x), 0) // 2) * 2) + ((max((b - y), 0) // 2) * 2)) + ((max((c - z), 0) // 2) * 2))
	if ((need * 2) <= extra):
	    global_list.append('Yes')
	else:
	    global_list.append('No')
	return global_list