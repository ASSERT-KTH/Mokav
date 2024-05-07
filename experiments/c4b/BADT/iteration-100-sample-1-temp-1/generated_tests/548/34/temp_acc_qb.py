def patched_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	sum = 0
	for i in range(1, (n + 1)):
	    sum = (sum + ((m + (i % 5)) // 5))
	global_list.append(sum)
	return global_list