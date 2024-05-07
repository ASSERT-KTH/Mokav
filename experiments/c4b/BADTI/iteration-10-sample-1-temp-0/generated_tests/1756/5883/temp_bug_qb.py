def original_func(*args):
	global_list = []
	
	a = list(args[0].split())
	b = []
	for i in range(len(a)):
	    if (a[i] not in b):
	        b += a[i]
	global_list.append((4 - len(b)))
	return global_list