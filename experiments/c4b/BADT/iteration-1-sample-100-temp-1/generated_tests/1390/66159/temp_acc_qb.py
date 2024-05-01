def patched_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split())
	g = ((c - ((b / a) * 100)) / (100 / a))
	if ((g > 0) and (int(g) != g)):
	    g = (int(g) + 1)
	(global_list.append(int(g)) if (g > 0) else global_list.append(0))
	return global_list