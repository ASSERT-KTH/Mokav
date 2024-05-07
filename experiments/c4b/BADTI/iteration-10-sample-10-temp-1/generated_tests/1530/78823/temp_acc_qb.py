def patched_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	global_list.append(('Impossible' if ((n == 0) and (m != 0)) else ('%d %d' % ((n + max(0, (m - n))), (n + max(0, (m - 1)))))))
	return global_list