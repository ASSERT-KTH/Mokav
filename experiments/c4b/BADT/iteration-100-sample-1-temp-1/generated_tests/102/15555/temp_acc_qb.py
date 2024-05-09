def patched_func(*args):
	global_list = []
	
	(a, b, ab) = map(int, args[0].split())
	global_list.append(min(((a + b) + ab), ((2 * a) + (2 * b)), ((2 * a) + (2 * ab)), ((2 * b) + (2 * ab))))
	return global_list