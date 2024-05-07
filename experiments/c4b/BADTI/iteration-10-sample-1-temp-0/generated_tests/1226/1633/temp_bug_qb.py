def original_func(*args):
	global_list = []
	
	n = int(args[0])
	string = args[1]
	pages = list(map(int, string.split()))
	d = 0
	a = 0
	while (a < n):
	    a += pages[(d % 7)]
	    d += 1
	global_list.append((d % 7))
	return global_list