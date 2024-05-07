def patched_func(*args):
	global_list = []
	
	(x, y, z) = map(int, args[0].split())
	global_list.append((4 * int((((((x * y) // z) ** 0.5) + (((x * z) // y) ** 0.5)) + (((z * y) // x) ** 0.5)))))
	return global_list