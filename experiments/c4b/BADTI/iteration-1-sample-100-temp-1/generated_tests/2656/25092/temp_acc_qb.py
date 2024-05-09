def patched_func(*args):
	global_list = []
	
	(n, k) = args[0].split(' ')
	k = int(k)
	cur = 0
	ans = 0
	great = False
	for c in reversed(n):
	    if (cur >= k):
	        great = True
	        break
	    if (c == '0'):
	        cur += 1
	    else:
	        ans += 1
	if great:
	    global_list.append(ans)
	else:
	    global_list.append((len(n) - 1))
	return global_list