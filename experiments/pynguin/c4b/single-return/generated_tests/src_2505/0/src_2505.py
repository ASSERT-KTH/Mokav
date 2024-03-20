def func(*args):
	
	import time
	t = time.time()
	(n, *arr) = list(map(int, args[0].split()))
	arr.sort()
	while ((time.time() - t) < 1.3):
	    pass
	return(' '.join(list(map(str, arr))))
