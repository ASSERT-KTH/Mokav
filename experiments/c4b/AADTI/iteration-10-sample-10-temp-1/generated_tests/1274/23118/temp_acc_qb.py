def patched_func(*args):
	global_list = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	count = 0
	for i in range(d):
	    if ((((i + 1) % k) == 0) or (((i + 1) % l) == 0) or (((i + 1) % m) == 0) or (((i + 1) % n) == 0)):
	        count += 1
	global_list.append(count)
	return global_list