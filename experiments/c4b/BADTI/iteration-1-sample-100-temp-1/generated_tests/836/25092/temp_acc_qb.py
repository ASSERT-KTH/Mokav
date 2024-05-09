def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	f1 = 1
	f2 = 1
	ans = (- 1)
	while (f2 <= n):
	    (f1, f2) = (f2, (f1 + f2))
	    ans += 1
	global_list.append(ans)
	return global_list