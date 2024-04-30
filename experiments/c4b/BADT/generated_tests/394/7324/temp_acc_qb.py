def patched_func(*args):
	global_list = []
	
	a = args[0].split()
	(x, y) = (int(a[0]), int(a[1]))
	out = 0
	while ((y > 0) and (x > 1)):
	    out += ((2 * x) - 3)
	    x -= 2
	    y -= 1
	global_list.append(out)
	return global_list