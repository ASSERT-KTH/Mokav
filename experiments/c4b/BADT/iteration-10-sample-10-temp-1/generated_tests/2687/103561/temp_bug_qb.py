def original_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].rstrip().split())
	if (n <= m):
	    global_list.append(n)
	else:
	    ans = m
	    n -= m
	    left = 0
	    right = (n + 1)
	    while ((right - left) > 1):
	        mid = (left + ((right - left) // 2))
	        if (n <= (((mid + 1) * mid) // 2)):
	            right = mid
	        else:
	            left = mid
	    global_list.append(right)
	return global_list