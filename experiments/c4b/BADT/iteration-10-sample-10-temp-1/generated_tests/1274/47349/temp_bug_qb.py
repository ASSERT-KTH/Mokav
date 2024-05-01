def original_func(*args):
	global_list = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	w = 0
	for x in range(1, d):
	    if (((x % k) == 0) or ((x % l) == 0) or ((x % m) == 0) or ((x % n) == 0)):
	        w += 1
	if ((k > d) and (l > d) and (m > d) and (n > d)):
	    w = 0
	global_list.append(w)
	return global_list