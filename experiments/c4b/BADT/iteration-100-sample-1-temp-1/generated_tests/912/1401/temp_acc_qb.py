def patched_func(*args):
	global_list = []
	
	(N, K) = map(int, args[0].split())
	rem = (240 - K)
	cnt = 5
	acc = 0
	ans = 0
	while (acc < rem):
	    if ((acc + cnt) <= rem):
	        acc += cnt
	        ans += 1
	        cnt = (5 * (ans + 1))
	    else:
	        break
	global_list.append(min(N, ans))
	return global_list