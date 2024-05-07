def original_func(*args):
	global_list = []
	
	n = int(args[0])
	n %= 4
	res = 6
	for i in range(1, (n + 1)):
	    res *= 8
	global_list.append((res % 10))
	return global_list