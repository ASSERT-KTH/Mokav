def original_func(*args):
	global_list = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	dragons = ([0] * d)
	for i in range(d):
	    if (((i % k) == 0) or ((i % l) == 0) or ((i % m) == 0) or ((i % n) == 0)):
	        dragons[i] = 1
	global_list.append(dragons.count(1))
	return global_list