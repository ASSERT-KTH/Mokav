def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	p = ((9 ** n) * (3 ** n))
	global_list.append(((p - (7 ** n)) % 1000000007))
	return global_list