def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if (n < 13):
	    global_list.append(pow(2, n))
	else:
	    num = pow(2, 12)
	    n = (n - 13)
	    ans = 8092
	    while n:
	        ans = (ans * 2)
	        n = (n - 1)
	    global_list.append(ans)
	return global_list