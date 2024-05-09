def original_func(*args):
	global_list = []
	
	(y, k, n) = map(int, args[0].split())
	a = (k - (y % k))
	if ((y + a) <= n):
	    if (a == 0):
	        global_list.append(' '.join((str(x) for x in [((t + 1) * k) for t in range(((n - y) // k))])))
	    else:
	        global_list.append(' '.join((str(x) for x in [(a + (t * k)) for t in range(((n - y) // k))])))
	else:
	    global_list.append((- 1))
	return global_list