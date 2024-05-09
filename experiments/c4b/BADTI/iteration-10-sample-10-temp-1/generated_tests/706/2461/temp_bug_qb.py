def original_func(*args):
	global_list = []
	
	(x, y) = map(int, args[0].split())
	(a, v) = (([x] * 3), 0)
	while (a[2] > y):
	    a[2] = max(((a[1] - a[0]) + 1), y)
	    a.sort()
	    v += 1
	global_list.append(v)
	return global_list