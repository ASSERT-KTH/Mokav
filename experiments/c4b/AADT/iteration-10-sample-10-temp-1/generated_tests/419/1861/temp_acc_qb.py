def patched_func(*args):
	global_list = []
	
	(n, a, b) = (int(i) for i in args[0].split())
	c = (abs(b) % n)
	if (b < 0):
	    r = (a - c)
	    if (r < 1):
	        r += n
	else:
	    r = (a + c)
	    if (r > n):
	        r -= n
	global_list.append(r)
	return global_list