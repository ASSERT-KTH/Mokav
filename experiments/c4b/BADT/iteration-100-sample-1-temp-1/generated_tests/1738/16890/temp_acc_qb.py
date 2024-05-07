def patched_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split())
	k = (((a * b) * c) ** 0.5)
	global_list.append((4 * int((((k / a) + (k / b)) + (k / c)))))
	return global_list