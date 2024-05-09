def patched_func(*args):
	global_list = []
	
	(n, a, b) = [int(i) for i in args[0].split()]
	h = 0
	for i in range(1, (n + 1)):
	    if (((i - 1) >= a) and ((n - i) <= b)):
	        h += 1
	global_list.append(h)
	return global_list