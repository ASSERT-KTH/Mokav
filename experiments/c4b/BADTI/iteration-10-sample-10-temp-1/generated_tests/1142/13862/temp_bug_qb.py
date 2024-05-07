def original_func(*args):
	global_list = []
	
	(n, a, b) = map(int, args[0].split())
	ans = min((n - a), (a + 1))
	global_list.append(ans)
	return global_list