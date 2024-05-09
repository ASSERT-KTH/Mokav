def patched_func(*args):
	global_list = []
	
	lis = []
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	d = int(args[3])
	e = int(args[4])
	for i in range(1, (e + 1), 1):
	    if (((i % a) == 0) or ((i % b) == 0) or ((i % c) == 0) or ((i % d) == 0)):
	        lis.append(i)
	global_list.append(len(lis))
	return global_list