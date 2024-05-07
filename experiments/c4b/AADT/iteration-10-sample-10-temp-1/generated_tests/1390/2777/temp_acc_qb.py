def patched_func(*args):
	global_list = []
	
	(n, x, y) = [int(i) for i in args[0].split()]
	ans = int((((y / 100) * n) - x))
	if (((ans + x) / n) < (y / 100)):
	    ans += 1
	if (ans > 0):
	    global_list.append(ans)
	else:
	    global_list.append(0)
	return global_list