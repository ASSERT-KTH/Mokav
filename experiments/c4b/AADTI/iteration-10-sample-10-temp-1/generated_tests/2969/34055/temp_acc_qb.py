def patched_func(*args):
	global_list = []
	
	read = (lambda : map(int, args[0].split()))
	(s, v1, v2, t1, t2) = read()
	f1 = ((t1 * 2) + (s * v1))
	f2 = ((t2 * 2) + (s * v2))
	global_list.append(('First' if (f1 < f2) else ('Second' if (f1 > f2) else 'Friendship')))
	return global_list