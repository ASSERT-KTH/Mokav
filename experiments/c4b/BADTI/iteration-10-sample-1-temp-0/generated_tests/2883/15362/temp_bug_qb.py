def original_func(*args):
	global_list = []
	
	(x1, y1, x2, y2) = map(int, args[0].split())
	(x, y) = map(int, args[1].split())
	if (((abs((x2 - x1)) % x) == 0) and ((abs((y2 - y1)) % y) == 0) and ((abs((x2 - x1)) % 2) == (abs((y2 - y1)) % 2))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list