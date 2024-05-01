def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	sum = 0
	s = 1
	while (int(bin(s)[2:]) <= n):
	    sum += 1
	    s += 1
	global_list.append(sum)
	return global_list