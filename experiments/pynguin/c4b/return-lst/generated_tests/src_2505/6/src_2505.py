def func(*args):
	ret_values = []
	
	import time
	t = time.time()
	(n, *arr) = list(map(int, args[0].split()))
	arr.sort()
	while ((time.time() - t) < 1.3):
	    pass
	ret_values.append(' '.join(list(map(str, arr))))

	return ret_values
