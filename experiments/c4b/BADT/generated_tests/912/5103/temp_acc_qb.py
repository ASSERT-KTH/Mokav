def patched_func(*args):
	global_list = []
	
	(n, k) = map(int, args[0].split())
	ans = 0
	while ((k + (5 * ans)) < 240):
	    k += (5 * ans)
	    ans += 1
	    if (ans == n):
	        break
	if ((k + (5 * ans)) > 240):
	    ans -= 1
	global_list.append(ans)
	return global_list