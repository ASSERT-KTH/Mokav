def patched_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	if (n <= m):
	    global_list.append(n)
	else:
	    lo = 1
	    hi = int(2000000000.0)
	    while (lo < hi):
	        mid = ((lo + hi) // 2)
	        val = (((mid + 1) * mid) // 2)
	        val1 = (((mid - 1) * mid) // 2)
	        if ((n - val) > m):
	            lo = mid
	        elif (((n - val) < m) and ((n - val1) < m)):
	            hi = mid
	        else:
	            break
	    if ((n - val1) <= m):
	        global_list.append(((m + mid) - 1))
	    elif ((n - val) <= m):
	        global_list.append((m + mid))
	return global_list