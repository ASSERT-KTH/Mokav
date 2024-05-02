def patched_func(*args):
	global_list = []
	
	(c, v0, v1, a, l) = map(int, args[0].split())
	sum1 = v0
	days = 1
	while (sum1 < c):
	    sum1 += min(((v0 + (days * a)) - l), (v1 - l))
	    days += 1
	global_list.append(days)
	return global_list