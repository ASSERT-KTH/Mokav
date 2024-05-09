def original_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	if (n <= m):
	    global_list.append(n)
	else:
	    aM = m
	    n = (n - m)
	    l = 0
	    r = 2000000000.0
	    while (l < r):
	        m = ((l + r) / 2)
	        val = ((m * (m + 1)) / 2)
	        if (val >= n):
	            r = m
	        else:
	            l = (m + 1)
	    global_list.append((l + aM))
	return global_list