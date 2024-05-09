def patched_func(*args):
	global_list = []
	
	[x1, y1, x2, y2] = [int(x) for x in args[0].split()]
	[x, y] = [int(x) for x in args[1].split()]
	global_list.append(['NO', 'YES'][(((((x2 - x1) / x) % 2) == (((y2 - y1) / y) % 2)) and (((x2 - x1) % x) == ((y2 - y1) % y) == 0))])
	return global_list