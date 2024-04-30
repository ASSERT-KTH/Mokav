def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if (n == 0):
	    global_list.append(1)
	else:
	    ans = 1
	    for i in range((n - 1)):
	        ans *= 3
	    global_list.append((ans % 1000003))
	return global_list