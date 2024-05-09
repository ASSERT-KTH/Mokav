def patched_func(*args):
	global_list = []
	
	(x1, y1, x2, y2) = [int(i) for i in args[0].split()]
	(x, y) = [int(i) for i in args[1].split()]
	if (((x1 % x) == (x2 % x)) and ((y1 % y) == (y2 % y)) and ((((x2 - x1) // x) % 2) == (((y2 - y1) // y) % 2))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list