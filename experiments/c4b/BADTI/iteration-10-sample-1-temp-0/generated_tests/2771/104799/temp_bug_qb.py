def original_func(*args):
	global_list = []
	
	(n, t, k, d) = [int(x) for x in args[0].split(' ')]
	time1 = 0
	if ((n % k) != 0):
	    time1 = int((((n // k) * t) + t))
	a = 0
	b = d
	while (n > 0):
	    if (a < b):
	        a = (a + t)
	    else:
	        b = (b + t)
	    n = (n - k)
	time2 = max(a, b)
	if (time1 > time2):
	    global_list.append('Yes')
	else:
	    global_list.append('No')
	return global_list