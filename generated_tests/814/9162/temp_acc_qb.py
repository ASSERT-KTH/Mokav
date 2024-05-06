def patched_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	x = 1
	while (0 != ((a * x) % 10) != b):
	    x = (x + 1)
	global_list.append(x)
	return global_list