def patched_func(*args):
	global_list = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	wyn = 0
	for x in range(1, (d + 1)):
	    if (((x % k) == 0) or ((x % l) == 0) or ((x % m) == 0) or ((x % n) == 0)):
	        wyn += 1
	global_list.append(wyn)
	return global_list