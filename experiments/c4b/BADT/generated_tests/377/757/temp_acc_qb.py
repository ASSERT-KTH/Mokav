def patched_func(*args):
	global_list = []
	
	(n, b) = tuple(map(int, args[0].split()))
	if (n > b):
	    (n, b) = (b, n)
	if ((n < 2) and (b < 2)):
	    global_list.append(0)
	else:
	    p = (b - n)
	    l = [(- 3), (- 1), 0]
	    global_list.append((((2 * (n + (p // 3))) + l[(p % 3)]) + (p // 3)))
	return global_list