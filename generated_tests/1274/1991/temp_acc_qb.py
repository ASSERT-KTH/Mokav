def patched_func(*args):
	global_list = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	ans = 0
	for a in range(1, (d + 1)):
	    if (((a % l) == 0) or ((a % k) == 0) or ((a % m) == 0) or ((a % n) == 0)):
	        ans = (ans + 1)
	global_list.append(ans)
	return global_list