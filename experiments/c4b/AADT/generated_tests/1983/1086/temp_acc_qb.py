def patched_func(*args):
	global_list = []
	
	import math
	n = int(args[0])
	ans = 0
	for x in range(1, n):
	    ans += (x * (n - x))
	ans += n
	global_list.append(ans)
	return global_list