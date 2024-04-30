def patched_func(*args):
	global_list = []
	
	from bisect import bisect_left
	arr = [(((((2 * i) + 1) ** 2) // 2) + 1) for i in range(7)]
	n = int(args[0])
	if (n == 3):
	    global_list.append(5)
	else:
	    global_list.append(((2 * bisect_left(arr, n)) + 1))
	return global_list