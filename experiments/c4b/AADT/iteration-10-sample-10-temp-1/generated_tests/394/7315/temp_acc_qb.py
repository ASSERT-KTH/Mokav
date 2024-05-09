def patched_func(*args):
	global_list = []
	
	(n, k) = list(map(int, args[0].split()))
	ans = ((n * (n - 1)) // 2)
	if (k >= (n // 2)):
	    global_list.append(ans)
	else:
	    m = (n - (2 * k))
	    ans = (ans - ((m * (m - 1)) // 2))
	    global_list.append(ans)
	return global_list