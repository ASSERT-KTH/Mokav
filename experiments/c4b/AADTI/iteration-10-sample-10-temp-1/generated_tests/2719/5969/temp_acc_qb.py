def patched_func(*args):
	global_list = []
	
	(x, y) = list(map(int, args[0].split()))
	a = True
	d = 1
	while a:
	    n = (x * 3)
	    m = (y * 2)
	    if (n > m):
	        global_list.append(d)
	        a = False
	    elif (m >= n):
	        d += 1
	        x = n
	        y = m
	return global_list