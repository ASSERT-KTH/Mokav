def original_func(*args):
	global_list = []
	
	(x1, y1) = map(int, args[0].split())
	(x2, y2) = map(int, args[1].split())
	if ((x2 < 0) or (y2 < 0)):
	    el = min(x2, y2)
	    global_list.append((abs(el) + min(x1, y1)))
	else:
	    global_list.append((max(x2, y2) - min(x1, y1)))
	return global_list