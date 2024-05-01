def original_func(*args):
	global_list = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	count = 0
	for i in range(d):
	    if (((i % k) == 0) or ((i % l) == 0) or ((i % m) == 0) or ((i % n) == 0)):
	        count += 1
	global_list.append(count)
	return global_list