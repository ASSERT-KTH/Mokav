def patched_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split())
	sum = []
	sum.append(((a + b) + c))
	sum.append(((a * 2) + (b * 2)))
	sum.append(((a * 2) + (c * 2)))
	sum.append(((b * 2) + (c * 2)))
	global_list.append(min(sum))
	return global_list