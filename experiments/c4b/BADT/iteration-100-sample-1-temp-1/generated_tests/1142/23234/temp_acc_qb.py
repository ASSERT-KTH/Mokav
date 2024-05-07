def patched_func(*args):
	global_list = []
	
	(n, a, b) = map(int, args[0].split())
	ans = (n - a)
	if (ans > (b + 1)):
	    ans = (b + 1)
	global_list.append(ans)
	return global_list