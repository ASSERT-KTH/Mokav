def patched_func(*args):
	global_list = []
	
	tl = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
	(n, m) = map(int, args[0].split())
	ans = (tl[(tl.index(n) + 1)] == m)
	global_list.append(['NO', 'YES'][ans])
	return global_list