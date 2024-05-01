def patched_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	b = ((240 - b) // 5)
	i = 0
	while ((i < a) and (b >= 0)):
	    i += 1
	    b -= i
	global_list.append((i - (b < 0)))
	return global_list