def patched_func(*args):
	global_list = []
	
	a = args[0]
	global_list.append((a.upper() if ((sum((a.count(x) for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')) * 2) > len(a)) else a.lower()))
	return global_list