def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	s = 'aabb'
	a = len(s)
	global_list.append(((s * (n // a)) + s[:(n % a)]))
	return global_list