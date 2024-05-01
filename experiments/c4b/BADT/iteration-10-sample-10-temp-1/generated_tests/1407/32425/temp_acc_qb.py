def patched_func(*args):
	global_list = []
	
	s = args[0]
	(a, b) = (s.split(' ')[0], s.split(' ')[1])
	global_list.append((int(a) + int(b[::(- 1)])))
	return global_list