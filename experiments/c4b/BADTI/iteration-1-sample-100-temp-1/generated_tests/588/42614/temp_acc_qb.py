def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if ((n % 2) == 1):
	    global_list.append((n // 2))
	else:
	    x = 1
	    while (x <= n):
	        x *= 2
	    global_list.append(((n - (x // 2)) // 2))
	return global_list