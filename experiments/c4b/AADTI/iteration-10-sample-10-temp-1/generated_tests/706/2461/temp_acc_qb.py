def patched_func(*args):
	global_list = []
	
	(x, y) = map(int, args[0].split())
	(a, v) = (([y] * 3), 0)
	while (a[0] < x):
	    a[0] = min(x, ((a[1] + a[2]) - 1))
	    a.sort()
	    v += 1
	global_list.append(v)
	return global_list