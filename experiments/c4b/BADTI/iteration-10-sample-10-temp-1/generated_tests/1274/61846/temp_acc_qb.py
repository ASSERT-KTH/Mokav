def patched_func(*args):
	global_list = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	count = 0
	for i in range(1, (d + 1)):
	    if (((i % k) != 0) and ((i % l) != 0) and ((i % m) != 0) and ((i % n) != 0)):
	        count += 1
	global_list.append((d - count))
	return global_list