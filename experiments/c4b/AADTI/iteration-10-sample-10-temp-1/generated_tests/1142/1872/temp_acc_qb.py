def patched_func(*args):
	global_list = []
	
	(n, a, b) = list(map(int, args[0].split()))
	ans = ((n - max((a + 1), (n - b))) + 1)
	global_list.append(ans)
	return global_list