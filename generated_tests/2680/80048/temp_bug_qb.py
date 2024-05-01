def original_func(*args):
	global_list = []
	
	import time
	(n, *arr) = list(map(int, args[0].split()))
	arr = list(set(arr))
	arr.sort()
	time.sleep(1)
	global_list.append(' '.join(list(map(str, arr))))
	return global_list