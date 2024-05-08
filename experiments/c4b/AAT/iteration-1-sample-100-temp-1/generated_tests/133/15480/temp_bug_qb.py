def original_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split())
	(x, y, z) = map(int, args[1].split())
	need = ((max((x - a), 0) + max((y - b), 0)) + max((z - c), 0))
	extra = ((max((a - x), 0) + max((b - y), 0)) + max((c - z), 0))
	if ((need * 2) <= extra):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list