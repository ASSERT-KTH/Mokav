def original_func(*args):
	global_list = []
	
	(n, k) = map(int, args[0].split())
	ans = 0
	while ((k + (5 * ans)) < 240):
	    ans += 1
	    k += (5 * ans)
	    if (ans == n):
	        break
	global_list.append(ans)
	return global_list