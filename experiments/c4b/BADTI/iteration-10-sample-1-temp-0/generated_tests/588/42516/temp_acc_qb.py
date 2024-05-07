def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if (n & 1):
	    global_list.append((n // 2))
	else:
	    k = 1
	    while (k <= n):
	        k *= 2
	    global_list.append(((n - (k // 2)) // 2))
	return global_list