def original_func(*args):
	global_list = []
	
	(n, k) = args[0].split(' ')
	k = int(k)
	cur = 0
	ans = 0
	for c in reversed(n):
	    if (cur >= k):
	        break
	    if (c == '0'):
	        cur += 1
	    else:
	        ans += 1
	global_list.append(ans)
	return global_list