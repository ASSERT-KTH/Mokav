def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	a = ((2 ** (len(str(n)) - 1)) - 1)
	i = 0
	while (int(bin(((2 ** (len(str(n)) - 1)) + i)).replace('b', '0')) <= n):
	    i += 1
	global_list.append((a + i))
	return global_list