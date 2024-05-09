def patched_func(*args):
	global_list = []
	
	import time
	t = time.time()
	(n, *arr) = list(map(int, args[0].split()))
	arr.sort()
	while ((time.time() - t) < 1.3):
	    pass
	global_list.append(' '.join(list(map(str, arr))))
	return global_list