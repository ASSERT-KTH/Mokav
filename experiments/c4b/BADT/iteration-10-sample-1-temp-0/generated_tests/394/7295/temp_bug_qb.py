def original_func(*args):
	global_list = []
	
	(n, k) = [int(i) for i in args[0].split()]
	ans = 0
	for i in range(k):
	    while (n >= 2):
	        ans += ((2 * n) - 3)
	        n -= 2
	global_list.append(ans)
	return global_list