def patched_func(*args):
	global_list = []
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	d = int(args[3])
	e = int(args[4])
	n = 0
	for i in range(1, (e + 1)):
	    if (((i % a) == 0) or ((i % b) == 0) or ((i % c) == 0) or ((i % d) == 0)):
	        n += 1
	global_list.append(n)
	return global_list