def patched_func(*args):
	global_list = []
	
	(n, k) = [int(i) for i in args[0].split()]
	if (k >= (n // 2)):
	    global_list.append(((n * (n - 1)) // 2))
	else:
	    ans = (((((n - 1) + n) - k) * k) // 2)
	    ans = ((ans * 2) - (k * k))
	    global_list.append(ans)
	return global_list