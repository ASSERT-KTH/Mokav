def patched_func(*args):
	global_list = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	drag = list(range(1, (d + 1)))
	count = 0
	for dr in drag:
	    if (((dr % k) == 0) or ((dr % l) == 0) or ((dr % m) == 0) or ((dr % n) == 0)):
	        count += 1
	global_list.append(count)
	return global_list